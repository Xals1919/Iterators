class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.result = [iter(self.list_of_list)]
        return self
    
    def __next__(self):
        while self.result:
            try:
                next_item = next(self.result[-1])
            except StopIteration:
                self.result.pop()
                continue
            if isinstance(next_item, list):
                self.result.append(iter(next_item))
            else:
                return next_item
        raise StopIteration

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item
        # print('в цикле все ок')

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    # print('все ок')

if __name__ == '__main__':
    test_3()