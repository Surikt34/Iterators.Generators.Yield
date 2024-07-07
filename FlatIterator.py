"""
Должен получиться итератор, который принимает список списков
и возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов.
Функция test в коде ниже также должна отработать без ошибок.
"""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Проверяем, есть ли еще элементы в списке
        while self.outer_index < len(self.list_of_list):
            # Проверяем, что текущий подсписок не пустой и у него есть еще элементы
            if self.inner_index < len(self.list_of_list[self.outer_index]):
                item = self.list_of_list[self.outer_index][self.inner_index]
                self.inner_index += 1
                return item
            # Переходим к следующему подсписку, если текущий подсписок исчерпан
            self.outer_index += 1
            self.inner_index = 0
        # Если все элементы были перебраны, вызываем  StopIteration
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    try:
        test_1()
        print('Тест прошел успешно')
    except AssertionError:
        print('Тест не пройден')
