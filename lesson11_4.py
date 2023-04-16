# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя

from time import time
from time import ctime


class Archive:
    """Save old value"""
    _instance = None

    def __init__(self, num: int, val: str):
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.number = []
            cls._instance.value = []
        else:
            cls._instance.number.append(cls._instance.num)
            cls._instance.value.append(cls._instance.val)
        return cls._instance

    def __str__(self):
        return f'Класс записывает число {self.num} и строку {self.val} в словарь'

    def __repr__(self):
        return f'(Archive {self.number}, {self.value})'