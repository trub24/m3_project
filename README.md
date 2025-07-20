GUI интерфейс для моделей:
ContentType User Group Permission

Последовательность запуска проекта:
docker build -t m3_project .
docker run --name m3_project --rm -p 8000:8000 m3_project

Получении доступа к приложению, запущенному в контейнере, с помощью веб-браузера по ссылке: http://localhost:8000