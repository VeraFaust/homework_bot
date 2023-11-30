# Бот-ассистент

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

- Установите зависимости из файла requirements.txt:
```
py -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

- Запустите файл homework.py.

## Примеры ответов от API:
```
{
   "homeworks":[
      {
         "id":124,
         "status":"rejected",
         "homework_name":"username__hw_python_oop.zip",
         "reviewer_comment":"Код не по PEP8, нужно исправить",
         "date_updated":"2020-02-13T16:42:47Z",
         "lesson_name":"Итоговый проект"
      },
      {
         "id":123,
         "status":"approved",
         "homework_name":"username__hw_test.zip",
         "reviewer_comment":"Всё нравится",
         "date_updated":"2020-02-11T14:40:57Z",
         "lesson_name":"Тестовый проект"
      },

      ...

   ],
   "current_date":1581604970
}
```

## Автор
Вера Фауст
