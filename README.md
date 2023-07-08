Мой первый проект на фреймворке Django для блогов с авторизацией (неавторизованные юзеры не могут добавлять посты), подключенной базой данных Postgres; 
Чтобы запустить проект в докер контейнере:
1. docker-compose run --rm blogsapp sh -c "python manage.py migrate"
2. docker-compose run --rm blogsapp sh -c "python manage.py createsuperuser"
