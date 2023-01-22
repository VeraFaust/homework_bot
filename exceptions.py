class ApiResponseError(Exception):
    """Исключение для некорректного ответа сервера"""
    pass


class StatusError(Exception):
    """Исключение для некорректного статуса"""
    pass

class ConversionError(Exception):
    """Ошибка конвертирования в Json"""
    pass