### Бот-ассистент

## Описание:
В этом проекте создан Telegram-bot, который помогает узнать статус домашней работы.  
Бот обращается к API сервису Практикум.Домашка и узнает статус домашней работы:
- reviewing: работа взята на ревью;
- approved: ревью успешно пройдено;
- rejected: работа проверена, но у ревьюера есть замечания.

## Пример ответа API:
{
   "id":123,
   "status":"approved",
   "homework_name":"username__hw_test.zip",
   "reviewer_comment":"Всё нравится",
   "date_updated":"2020-02-11T14:40:57Z",
   "lesson_name":"Тестовый проект"
}

## Технологии:
- API;
- REST;
- HTTP;
- Client API;
- Bot API.

## Запуск проекта:
- Клонируйте репозиторий:
```
git clone https://github.com/VeraFaust/homework_bot.git
```

- Установите и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```

- Установите зависимости из файла requirements.txt
```
py -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- 
Перейти по ссылке:
На сайт http://127.0.0.1:8000/  
В админ-зону http://127.0.0.1:8000/admin

Остановить работу:
```
Ctrl+C
```

## Автор
Вера Фауст
