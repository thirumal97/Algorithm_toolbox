# addition of two numbers

def addition_sum(a, b):
    return a+b

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(addition_sum(a, b))