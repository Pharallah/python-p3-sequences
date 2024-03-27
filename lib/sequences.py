#!/usr/bin/env python3

# def print_fibonacci(length):
#     if length == 0:
#         fibonacci_sequence.clear()
#     elif length == 1:
#         fibonacci_sequence.pop()
#     else:
#         fibonacci_sequence = [0, 1]
#         while len(fibonacci_sequence) < length:
#             next_sequence = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#             fibonacci_sequence.append(next_sequence)

#     print(fibonacci_sequence)

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < length:
            next_sequence = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_sequence)
        print(fibonacci_sequence)
