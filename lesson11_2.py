# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-
# архивов
# list-архивы также являются свойствами экземпляра

class Archive:
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


if __name__ == '__main__':
    s = Archive(123, 'run1')
    print(s.number, s.value)
    s = Archive(456, 'run2')
    print(s.number, s.value)
    s = Archive(789, 'run3')
    print(s.number, s.value)
