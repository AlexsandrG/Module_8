class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    pass

def generate_exception(num):
    if num == 1:
        raise InvalidDataException("Произошло исключение неверных данных!")
    elif num == 2:
        raise ProcessingException("Произошло исключение обработки!")
    else:
        print("Исключение не было вызвано.")

try:
    generate_exception(1)
except InvalidDataException as e:
    print(f"Поймано исключение InvalidDataException: {e}")

try:
    generate_exception(2)
except ProcessingException as e:
    print(f"Поймано исключение ProcessingException: {e}")

try:
    generate_exception(3)
except (InvalidDataException, ProcessingException) as e:
    print(f"Поймано пользовательское исключение: {e}")
finally:
    print(f'закрыли открытые файлы')