import sys

from functools import reduce
from operator import add, mul

def hex_to_binary(input):
  output = bin(int(input, 16))[2:]
  return "0"*(len(input)*4 - len(output)) + output

def parse_packet(binary):
  # Returned values (includes composition of sub-packets)
  numbers = []
  cur_offset = 0
  sum_versions = 0

  V = int(binary[:3], 2)
  sum_versions += V
  T = int(binary[3:6], 2)

  # Type of 4 represents a literal number.
  if T == 4:
    all_parts = []
    start = 6
    while True:
      all_parts.append(binary[start+1:start+5])
      if binary[start] == "0":
        break
      start = start + 5
    numbers.append(int("".join(all_parts), 2))
    return numbers, start + 5, V
  else:
    I = int(binary[6], 2)
    if I == 0:
      L = int(binary[7:22], 2)
      cur_offset = 22
      while cur_offset < 22 + L:
        vals, offset, version = parse_packet(binary[cur_offset:])
        sum_versions += version
        cur_offset = cur_offset + offset
        for val in vals:
          numbers.append(val)
    else:
      L = int(binary[7:18], 2)
      i = 0
      cur_offset = 18
      while i < L:
        vals, offset, version = parse_packet(binary[cur_offset:])
        sum_versions += version
        cur_offset = cur_offset + offset
        i += 1
        for val in vals:
          numbers.append(val)
    if T == 0:
      return [reduce(add, numbers)], cur_offset, sum_versions
    elif T == 1:
      return [reduce(mul, numbers)], cur_offset, sum_versions
    elif T == 2:
      return [reduce(min, numbers)], cur_offset, sum_versions
    elif T == 3:
      return [reduce(max, numbers)], cur_offset, sum_versions
    elif T == 5:
      return [1 if numbers[0] > numbers[1] else 0], cur_offset, sum_versions
    elif T == 6:
      return [1 if numbers[0] < numbers[1] else 0], cur_offset, sum_versions
    elif T == 7:
      return [1 if numbers[0] == numbers[1] else 0], cur_offset, sum_versions

def main():
  for line in sys.stdin:
    vals, offset, sum_versions = parse_packet(hex_to_binary(line.strip()))
    print(vals[0])
    # print(sum_versions)

if __name__ == "__main__":
  main()
