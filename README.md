# Тестовое задание Kodland

**Задача**. Разработать блог на Python3 и Django, используя БД PostgreSQL и фронтенд фреймворк Materialize.

**Демонстрация**. Запустить контейнер СУБД, создать схему базы данных и запустить приложение.
```
docker-compose up -d db
docker-compose run --rm app python3 manage.py migrate
docker-compose up app
```

Начальная страница приложения будет доступна по адресу [http://localhost:8000](http://localhost:8000) Форма публикации -- [http://localhost:8000/blog/publish/](http://localhost:8000/blog/publish/)

Очистить окружение (в том числе удалить образы и тома) затем можно командой `docker-compose down --rmi all -v`
