def some_function(number: int, name: str) -> None:
    print("%s entered %s" % (name, number))

print(some_function(13, 'Mike'))
# Mike entered 13


def process_data(my_list, name):
    if name in my_list:
        return True
    else:
        return False

if __name__ == '__main__':
    my_list = ['Mike', 'Nick', 'Toby']
    print(process_data(my_list, 'Mike'))
    print(process_data(my_list, 'John'))
    # True
    # False

def process_data2(my_list: list, name: str) -> bool:
    return name in my_list

if __name__ == '__main__':
    my_list = ['Mike', 'Nick', 'Toby']
    print(process_data2(my_list, 'Mike'))
    print(process_data2(my_list, 'John'))
    # True
    # False


class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

def salad(fruit_one: Fruit, fruit_two: Fruit) -> list:
    print(fruit_one.name)
    print(fruit_two.name)
    return [fruit_one, fruit_two]

if __name__ == '__main__':
    f = Fruit('orange', 'orange')
    f2 = Fruit('apple', 'red')
    salad(f, f2)
    # orange
    # apple


Animal = str

def zoo(animal: Animal, number: int) -> None:
    print("The zoo has %s %s" % (number, animal))

if __name__ == '__main__':
    zoo('Zebras', 10)
    # The zoo has 10 Zebras