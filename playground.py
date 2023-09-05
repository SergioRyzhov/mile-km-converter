def add(*args):
    return sum(args)


numbers = input("Input coma separated numbers: ")

numbers = numbers.split(",")
numbers = list(map(int, numbers))

print(add(*numbers))
