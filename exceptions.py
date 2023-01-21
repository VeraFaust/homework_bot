class ApiResponseError(Exception):
    """Исключение для некорректного ответа сервера"""
    pass


class MessageSendingError(Exception):
    """Исключение для неотправленного сообщения"""
    pass


class StatusError(Exception):
    """Исключение для некорректного статуса"""
    pass