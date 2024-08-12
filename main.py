class FlatIterator:
    """Итератор для списков с одним уровнем вложенности"""
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list = 0
        self.current_element = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list >= len(self.list_of_list):
            raise StopIteration
        
        
        if self.current_element >= len(self.list_of_list[self.current_list]):
            self.current_list += 1
            self.current_element = 0
            return self.__next__()
        
        item = self.list_of_list[self.current_list][self.current_element]
        print(f"FI item: {item}")
        self.current_element += 1
        return item
    
class DeepFlatIterator:
    """Итератор для списков с любым уровнем вложенности"""
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.stack = [(list_of_list, 0)]  # Стек для хранения текущего списка и индекса

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_list, current_index = self.stack[-1]

            if current_index >= len(current_list):
                self.stack.pop()
                continue

            self.stack[-1] = (current_list, current_index + 1)
            item = current_list[current_index]

            if isinstance(item, list):
                self.stack.append((item, 0))
            else:
                print(f"DFI item: {item}")
                return item

        raise StopIteration

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

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            DeepFlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        
        assert flat_iterator_item == check_item

    assert list(DeepFlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']



if __name__ == '__main__':
    test_1()
    test_3()