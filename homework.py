import logging
import os
import sys
import datetime
import time
from http import HTTPStatus

import telegram
import requests
from exceptions import ApiResponseError, StatusError

from dotenv import load_dotenv
load_dotenv()


PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

RETRY_PERIOD = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - '
    '%(funcName)s - %(lineno)d - %(message)s'
)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(format)
logger.addHandler(handler)

HOMEWORK_VERDICTS = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


def check_tokens():
    """Доступность переменных окружения,."""
    """необходимых для работы программы."""
    tokens = [
        PRACTICUM_TOKEN,
        TELEGRAM_TOKEN,
        TELEGRAM_CHAT_ID
    ]
    if not all(tokens):
        message = 'Переменная окружения остуствует или не задана'
        logger.critical(message)
        return False
    return True


def send_message(bot, message):
    """Отправление сообщения в Telegram чат."""
    try:
        bot.send_message(
            TELEGRAM_CHAT_ID,
            message
        )
        logger.debug('Сообщение отправлено')
    except Exception as error:
        logger.error(f'Сообщение не отправлено. {error}')


def get_api_answer(timestamp):
    """Запрос к единственному эндпоинту API-сервиса."""
    params = {'from_date': timestamp}
    REQUEST = {
        'endpoint': ENDPOINT,
        'headers': HEADERS,
        'params': params
    }
    try:
        response = requests.get(REQUEST)
    except Exception as error:
        raise ApiResponseError(f'Ошибка при запросе к основному API: {error}')
    if response.status_code != HTTPStatus.OK:
        raise ApiResponseError('Ошибка при запросе к основному API.')
    logger.debug('Получен ответ от сервера')
    response = response.json()
    return response


def check_response(response):
    """Проверка ответа API на соответствие документации."""
    if not isinstance(response, dict):
        raise TypeError('Ответ сервера содержит неправильный тип данных')
    if ('homeworks' or 'current_date') not in response:
        raise KeyError('Ответ сервера не содержит нужных ключей')
    homeworks = response['homeworks']
    if not isinstance(homeworks, list):
        raise TypeError('В ответе сервера есть неправильный тип данных')
    logger.debug('Ответ сервера правильный!')
    return homeworks


def parse_status(homework):
    """Извлечение информации о д/з статус этой работы."""
    if 'homework_name' not in homework:
        raise KeyError('Ответ сервера не содержит нужных ключей')
    homework_status = homework.get('status')
    if homework_status not in HOMEWORK_VERDICTS:
        raise StatusError('Не корректный статус работы')
    homework_name = homework.get('homework_name')
    verdict = HOMEWORK_VERDICTS.get(homework_status)
    return f'Изменился статус проверки работы "{homework_name}". {verdict}'


def main():
    """Основная логика работы бота."""
    if not check_tokens():
        sys.exit()
    current_timestamp = int(time.time())
    previous_message = None
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    logger.info('Установлена связь с ботом!')
    now = datetime.datetime.now()
    send_message(
        bot,
        f'Бот начал работу: {now.strftime("%d-%m-%Y %H:%M")}')
    while True:
        try:
            response = get_api_answer(current_timestamp)
            homeworks = check_response(response)
            if homeworks:
                message = parse_status(homeworks[0])
            else:
                message = 'Обновлений по домашней работе нет'
                logger.debug(message)
            if message != previous_message:
                logger.info('Новое сообщение')
                send_message(bot, message)
                previous_message = message
            else:
                logger.info('Нового сообщения нет')
            try:
                current_timestamp = response['current_date']
            except KeyError:
                current_timestamp = int(time.time())
                logger.debug(
                    'Не удалось получить время запроса из ответа от API'
                    'Для выполнения следующего запроса принято текущее время'
                )
            else:
                logger.info('Время запроса получено из ответа от API.')

            time.sleep(RETRY_PERIOD)
            logger.debug(
                'Программа работает. Предыдущий запрос выполнен успешно'
            )
        except Exception as error:
            message = f'Сбой в работе программы: {error}'
            logger.error(message)

            time.sleep(RETRY_PERIOD)
        finally:
            logger.info('Новый запрос')


if __name__ == '__main__':
    main()
