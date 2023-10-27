# #первый вариант
# class FlatIterator:

#     def __init__(self, list_of_list):
#         self.list_of_list = list_of_list

#     def __iter__(self):
#         self.index_1 = 0
#         self.index_2 = 0
#         return self

#     def __next__(self):
#         if self.index_1 >= len(self.list_of_list):
#             raise StopIteration
#         self.item_1 = self.list_of_list[self.index_1]
#         self.item_2 = self.item_1[self.index_2]
#         self.index_2 += 1
#         if self.index_2 >= len(self.item_1):
#             self.index_1 += 1
#             self.index_2 = 0
#         return self.item_2

#второй вариант
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.result = iter([])
        self.index = 0
        return self

    def __next__(self):
        try:
            next_item = next(self.result)
        except StopIteration:
            if self.index >= len(self.list_of_list):
                raise StopIteration
            self.result = iter(self.list_of_list[self.index])
            self.index += 1
            next_item = next(self.result)
        return next_item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
        # print('в цикле все ок')

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    # print('все ок')


if __name__ == '__main__':
    test_1()