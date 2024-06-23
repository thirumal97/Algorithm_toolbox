# Input: An integer n and a sequence of n non-negative integers.
# Output: The maximum value that can be obtained by multiplying two different elements from
# the sequence.

def max_pairwise(list_b):
    print(list_b)
    new_b = sorted(list_b)
    print(new_b)
    return new_b[-1]*new_b[-2]



if __name__ == "__main__":
    a = int(input())
    list_b = list(map(int, input().split()))
    print(a)
    print(list_b)
    print(max_pairwise(list_b))


        