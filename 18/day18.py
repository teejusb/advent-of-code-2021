import sys
from math import ceil, floor

def parse_input(line, offset=0):
  l = []
  cur_num = []

  offset += 1  # Skip opening brace
  while line[offset] != ']':
    if line[offset] == '[':
      # Found a new list, so recurse
      sub_list, offset = parse_input(line, offset)
      l.append(sub_list)
      if line[offset] == ",":
        offset += 1
    elif line[offset] != ',':
      # Found a new number, add to list of digits.
      cur_num.append(line[offset])
      offset += 1
    else:
      # Actually create a number out of the list of digits.
      num = int("".join(cur_num))
      l.append(num)
      cur_num.clear()
      offset += 1
  
  # Add the last number if needed.
  if len(cur_num):
    l.append(int("".join(cur_num)))
  
  # Skip the closing brace.
  offset += 1
  return l, offset

def explode(sf, depth=0, l_val=None, r_val=None, can_explode=True):
  # Base case #1 -- Just add the respective number.
  # Only one of l_val or r_val might contain a value.
  if type(sf) == int:
    to_add = 0
    if l_val:
      to_add = l_val
    elif r_val:
      to_add = r_val
    return sf + to_add, None, None, False
  
  # Base case #2 -- Split up the snailfish if we've reached the depth.
  if depth == 4 and can_explode:
    return 0, sf[0], sf[1], True

  # Handle left subtree
  l_sf, l_l, l_r, l_exploded = explode(sf[0], depth + 1, l_val, None, can_explode)

  if l_exploded:
    l_val = l_r
    r_val = None
    can_explode = False
  else:
    l_val = False
  
  # Handle right subtree
  r_sf, r_l, r_r, r_exploded = explode(sf[1], depth + 1, l_val, r_val, can_explode)

  if r_exploded:
    l_sf, _, _, _ = explode(sf[0], depth + 1, None, r_l, False)
    return [l_sf, r_sf], None, r_r, True
  elif l_exploded:
    return [l_sf, r_sf], l_l, None, True
  else:
    return [l_sf, r_sf], None, None, False


def split(sf, can_split=True):
  if type(sf) == int:
    if can_split and sf >= 10:
      return [floor(sf / 2), ceil(sf/ 2)], True
    else:
      return sf, False
  
  left, l_split = split(sf[0], can_split)
  right, r_split = split(sf[1], not l_split and can_split)

  return [left, right], l_split or r_split


def add(x, y):
  sum = [x, y]
  exploded = True
  while exploded:
    sum, _, _, exploded = explode(sum)
    if not exploded:
      sum, exploded = split(sum)
  return sum


def score(sf):
  if type(sf) == int:
    return sf
  else:
    return score(sf[0]) * 3 + score(sf[1]) * 2


def main(part_two):
  sfs = []
  for line in sys.stdin:
    sfs.append(parse_input(line.strip())[0])
  
  if not part_two:
    sum = sfs[0]
    for sf in sfs[1:]:
      sum = add(sum, sf)

    print(score(sum))
  else:
    ans = 0
    for i in range(len(sfs)):
      for j in range(i + 1, len(sfs)):
        ans = max(
          ans,
          score(add(sfs[i], sfs[j])),
          score(add(sfs[j], sfs[i])),
        )
    print(ans)


if __name__ == "__main__":
  main(True)
