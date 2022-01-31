"""
3 implementations of fibonnaci.
"""


def fibonacci_recursive(num):
    if num in (0, 1):
        return num

    return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)


def fibonacci_imperative(num):
    if num in (0, 1):
        return num

    old = 0
    new = 1
    for _ in range(2, num+1):
        temp = old + new

        old = new
        new = temp
    return new

def main():

    for i in range(8):
        print(fibonacci_recursive(i), end=" ")
    for i in range(8):
        print(fibonacci_imperative(i), end=" ")


if __name__ == '__main__':
    main()
