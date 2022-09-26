# test_repository 
PostgreSQL + smtp сервис + FTP сервис

![image](https://d1q6f0aelx0por.cloudfront.net/product-logos/library-postgres-logo.png)

Сборка проекта <br>
$ docker-compose build

Запуск проекта <br>
$ docker-compose up

Для доступа в PostgreSQL <br>
Создается пользователь: postgres <br>
Пароль: 554455

Сервис SMTP запускается и автоматически подгружает данные

FTP разворачивается автоматически:

![image](https://user-images.githubusercontent.com/61121043/192363262-afdf964c-d592-4067-ad54-e84c07724ef8.png)


Останавливаем и удаляем контейнеры <br>
$ docker-compose down
