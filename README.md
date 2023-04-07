# api_final_yatube 

 

## Описание 

 

Это API сервиса YaMDB, собирающего отзывы пользователей на различные произведения. Поддерживает регистрацию пользователей, создание записей произведений, их категорий, жанров. Возможно оставление пользователями отзывов к произведениям с выставлением оценки от 1 до 10 и комментариев к отзывам.

 

## Стек технологий 

 

Проект использует django 3.2, djangorestframework 3.12.4, django-filter. Аутентификация посредством JWT-токенов с использованием PyJWT.
Разбит на контейнеры с помощью docker-compose. 

## Шаблон наполнения файла .env

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<имя пользователя в postgres>
POSTGRES_PASSWORD=<пароль пользователя в postgres>
DB_HOST=db
DB_PORT=5432 
```

## Как запустить проект: 

 

Клонировать репозиторий и перейти в него в командной строке: 

 

``` 

git clone git@github.com:Arhonist/infra_sp2.git

``` 

 

``` 

cd infra_sp2/infra

``` 

 

Соберите контейнеры и запустите их: 

 

``` 

docker-compose up -d --build

``` 

Перейдите в контейнер infra_web_1:

``` 
sudo docker exec -it infra_web_1 bash

``` 

Выполните миграции:

``` 
python manage.py migrate

``` 

Создайте суперюзера: 

``` 
python manage.py createsuperuser

``` 

Выполните collectstatic:

``` 
python manage.py collectstatic --no-input

``` 


## Документация 

 
Документация проекта сгенерирована с помощью ReDoc и доступна после запуска проекта по эндпоинту http://localhost/redoc/



## Credits

Над проектом работали:
- Аушев Никита - https://github.com/Arhonist - отзывы, рейтинги, комментарии, фильтрация, поиск, вьюсеты (тимлид команды);
- Голиков Александр - https://github.com/TheUncannyMrBean - система регистрации, авторизации, пользователи, пермишны;
- Николаева Татьяна - https://github.com/tanyanikolaeva21 - категории, жанры, тайтлы.
