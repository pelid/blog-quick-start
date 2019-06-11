# Заготовка для блога

Это заготовка для нового проекта — блога. В репозитории лежит Django проект с готовым фронтендом. За основу взята тема к Boostrap 4 [Artika HTML](https://github.com/prianto/artika-html).

![Artika HTML Preview](docs/preview.jpg?raw=true "Artika HTML")

# Как установить

Желательно воспользоваться одним из менеджеров виртуальных окружений [virtualenv](https://pypi.org/project/virtualenv/). Если не знаком с ним, то пропустите этот шаг.

Установите пакеты:

```bash
pip install -r requirements.txt
```

Перейдите в каталог `src` и запустите отладочный сервер:

```bash
cd src
python manage.py runserver
```

После того, как сервер заработает, откройте страницу в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).