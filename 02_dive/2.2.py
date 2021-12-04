#!/usr/bin/env python

with open('input.txt') as fh:
  instructions = fh.readlines()

position = 0
depth = 0
aim = 0


for line in instructions:
  if not line.strip():
    continue

  command, value = line.strip().split(' ')
  value = int(value)

  if command == 'forward':
    position += value
    depth += aim * value
    if depth < 0:
      depth = 0 # our submarine cannot fly
  elif command == 'up':
    aim -= value
  elif command == 'down':
    aim += value
  else:
    continue

print(depth * position)
