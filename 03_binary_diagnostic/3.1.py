#!/usr/bin/env python
bit_count = [0] * 12

with open('input.txt') as fh:
    report = fh.read().strip().split('\n')

for line in report:
    for i, bit in enumerate(line):
        if bit == '1':
            bit_count[i] += 1

gamma_bits = ''.join(['1' if bit_count[i] > len(report)/2 else '0' for i in range(0, 12) ])
epsilon_bits = ''.join(['0' if bit_count[i] > len(report)/2 else '1' for i in range(0, 12) ])

gamma = int(gamma_bits, 2)
epsilon = int(epsilon_bits, 2)

print(gamma * epsilon)
