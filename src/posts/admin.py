from django.contrib import admin
from django.conf import settings

from gdrive import api

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def upload_google_doc(self, post):
        google_scope = [
            # 'https://www.googleapis.com/auth/spreadsheets', # disabled
            'https://www.googleapis.com/auth/drive',
        ]

        gdrive_api = api.auth_in_google_drive(google_scope, settings.GAPI_CREDENTIALS_FILEPATH)

        title, article_html = api.get_article_html(gdrive_api, post.google_doc_id)

        post.html = article_html
        post.title = title
        post.save()

    def response_change(self, request, obj):
        response = super().response_change(request, obj)
        if obj.google_doc_id:
            self.upload_google_doc(obj)
        return response

    def response_add(self, request, obj, post_url_continue=None):
        response = super().response_add(request, obj, post_url_continue)
        if obj.google_doc_id:
            self.upload_google_doc(obj)
        return response
