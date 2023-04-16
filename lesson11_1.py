# lesson11_1.py
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)


from time import time
from time import ctime


class MyStr(str):
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author.capitalize()
        instance.time = ctime(time())
        return instance


if __name__ == '__main__':
    s = MyStr('My first class MyStr', 'Alexander')
    print(s)
    print(s.author)
    print(s.time)
