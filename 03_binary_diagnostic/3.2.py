#!/usr/bin/env python
import sys

with open('input.txt') as fh:
    report = fh.read().strip().split('\n')

def filter_list(source_list, bit, most_common=True):
  zero_list = []
  one_list = []

  for byte in source_list:
      if byte[bit] == '1':
          one_list.append(byte)
      else:
          zero_list.append(byte)

  if most_common:
      if len(one_list) == len(zero_list):
          return one_list
      return zero_list if len(zero_list) > len(one_list) else one_list
  else:
      if len(one_list) == len(zero_list):
          return zero_list
      return zero_list if len(zero_list) < len(one_list) else one_list

o2_rating_report = list(report)
for i in range(0, 12):
    o2_rating_report = filter_list(o2_rating_report, i)
    if len(o2_rating_report) == 1:
        break

co2_scrubber_report = list(report)
for i in range(0, 12):
    co2_scrubber_report = filter_list(co2_scrubber_report, i, most_common=False)
    if len(co2_scrubber_report) == 1:
        break

print( int(o2_rating_report[0], 2) * int(co2_scrubber_report[0], 2) )
