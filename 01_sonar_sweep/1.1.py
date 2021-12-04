#!/usr/bin/env python

with open('input.txt') as fh:
  data = [int(x) for x in fh.read().strip().split('\n')]

previous_measurement = None
count = 0

for measurement in data:
    if previous_measurement is None:
      previous_measurement = value
      continue

    if value > previous_measurement:
      count += 1

    previous_measurement = value

print(count)
