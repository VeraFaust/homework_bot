### Бот-ассистент

## Описание:
В этом проекте создан Telegram-bot, который помогает узнать статус домашней работы.  
Бот обращается к API сервису Практикум.Домашка и узнает статус домашней работы:
- reviewing: работа взята на ревью;
- approved: ревью успешно пройдено;
- rejected: работа проверена, но у ревьюера есть замечания.

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

- Запустите файл homework.py.

## Пример ответа API:
"homeworks":[  
   {  
        "id":123,  
        "status":"approved",  
        "homework_name":"username__hw_test.zip",  
        "reviewer_comment":"Всё нравится",  
        "date_updated":"2020-02-11T14:40:57Z",  
        "lesson_name":"Тестовый проект"  
     }
]

## Автор
Вера Фауст
