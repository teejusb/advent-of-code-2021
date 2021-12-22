import sys

from collections import defaultdict


# Do some fun set/bit manipulation.
def create_cipher(patterns):
    # Known digits
    one = patterns[2][0]
    seven = patterns[3][0]
    four = patterns[4][0]
    eight = patterns[7][0]

    def Value(s):
      return next(iter(s))

    cipher = {}

    a = one ^ seven
    cipher[Value(a)] = "a"

    seven_or_four = seven | four
    for pattern in patterns[6]:
      g = pattern - seven_or_four
      if len(g) == 1:
        nine = pattern
        e = eight - nine
        seven_or_g = seven | g
        seven_or_g_or_e = seven | g | e

        cipher[Value(g)] = "g"
        cipher[Value(e)] = "e"
        break

    for pattern in patterns[6]:
      b = pattern - seven_or_g_or_e
      if len(b) == 1:
        cipher[Value(b)] = "b"
        zero = pattern
        break
    
    for pattern in patterns[5]:
      d = pattern - seven_or_g
      if len(d) == 1:
        cipher[Value(d)] = "d"
        break

    a_b_d_e_g = a | b | d | e | g
    for pattern in patterns[6]:
      f = pattern ^ a_b_d_e_g
      if len(f) == 1:
        cipher[Value(f)] = "f"
        six = pattern
        break
    c = six ^ eight
    cipher[Value(c)] = "c"

    return cipher


def main():
  count = 0
  digits = {
    'abcefg' : "0",
    'cf' : "1",
    'acdeg': "2",
    'acdfg': "3",
    'bcdf': "4",
    'abdfg': "5",
    'abdefg': "6",
    'acf': "7",
    'abcdefg': "8",
    'abcdfg': "9",
  }

  count = 0
  total = 0
  for line in sys.stdin:
    pattern, values = line.strip().split(" | ")
    pattern = pattern.split(" ")
    values = values.split(" ")

    patterns = defaultdict(list)
    for segments in pattern:
      patterns[len(segments)].append(frozenset(segments))
    
    cipher = create_cipher(patterns)
    
    nums = []
    for value in values:
      segments = []
      for c in value:
        segments.append(cipher[c])
      digit = digits["".join([c for c in sorted(segments)])]
      if digit == "1" or digit == "4" or digit == "7" or digit == "8":
        count += 1
      nums.append(digit)
    total += int("".join(nums))
      
  print(count)
  print(total)


if __name__ == "__main__":
  main()
