#!/usr/bin/env python

with open('input.txt') as fh:
  instructions = fh.readlines()

position = 0
depth = 0

for line in instructions:
  if not line.strip():
    continue

  command, value = line.strip().split(' ')
  value = int(value)

  if command == 'forward':
    position += value
  elif command == 'up':
    depth -= value
  elif command == 'down':
    depth += value
  else:
    continue

print(depth * position)
