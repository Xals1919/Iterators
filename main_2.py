import types


def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
        # print('в цикле все ок')

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    # print('все ок')
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    # print('и тут все ок')


if __name__ == '__main__':
    test_2()
    