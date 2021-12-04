#!/usr/bin/env python

with open('input.txt') as fh:
  data = fh.readlines()

previous_measurement = None
count = 0

for measurement in data:
    if not measurement.strip():
      continue

    value = int(measurement.strip())
    if previous_measurement is None:
      previous_measurement = value
      continue

    if value > previous_measurement:
      count += 1

    previous_measurement = value

print(count)


