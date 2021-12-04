#!/usr/bin/env python

with open('input.txt') as fh:
  data = fh.readlines()

previous_window = None
row_count = 0
num_states = 4
sliding_windows = [0] * num_states
increase_count = 0

for measurement in data:
    measurement = measurement.strip()
    if not measurement:
      continue

    value = int(measurement)

    row_count += 1
    finalized_window = row_count % num_states

    if row_count < num_states:
      for i in range(0, row_count):
        sliding_windows[i] += value
    else:
      if previous_window is not None and sliding_windows[finalized_window] > previous_window:
        increase_count += 1
      previous_window = sliding_windows[finalized_window]
      sliding_windows[finalized_window] = 0
      for i in range(0, num_states):
        if i != finalized_window:
          sliding_windows[i] += value

if previous_window is not None and sliding_windows[(row_count+1) % num_states] > previous_window:
  increase_count += 1

print(increase_count)
