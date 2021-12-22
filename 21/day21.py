import sys
from functools import lru_cache


def part_one():
  game = {}
  for line in sys.stdin:
    parts = line.strip().split()
    game[int(parts[1])] = {
      "pos": int(parts[-1]),
      "score": 0,
    }
  
  cur_player = 1
  dice_roll = 1
  while True:
    sum_rolls = (dice_roll + 1) * 3
    dice_roll += 3

    game[cur_player]["pos"] = ((game[cur_player]["pos"] - 1) + sum_rolls) % 10 + 1
    game[cur_player]["score"] += game[cur_player]["pos"]
    if game[cur_player]["score"] >= 1000:
      break
    cur_player = 3 - cur_player
  # Switch to losing player
  cur_player = 3 - cur_player

  print(game[cur_player]["score"] * (dice_roll - 1))


DP = [
  [
    [
      [
        [0,0] for _ in range(31)
      ] for _ in range(31)
    ] for _ in range(11)
  ] for _ in range(11)
]


SUMS = {}

for roll1 in range(1, 4):
  for roll2 in range(1, 4):
    for roll3 in range(1, 4):
      total = roll1 + roll2 + roll3
      if not SUMS.get(total, None):
        SUMS[total] = 0
      SUMS[total] += 1


@lru_cache(maxsize=None)
def recurse(p1_pos, p2_pos, p1_score, p2_score, roll, cur_player):
  x,y = DP[p1_pos][p2_pos][p1_score][p2_score]
  if x != 0 and y != 0:
    return DP[p1_pos][p2_pos][p1_score][p2_score]
    
  cur_pos = p1_pos if cur_player == 1 else p2_pos
  cur_score = p1_score if cur_player == 1 else p2_score

  new_pos = ((cur_pos - 1) + roll) % 10 + 1   

  if cur_player == 1:
    p1_pos = new_pos
    p1_score = cur_score + new_pos
  else:
    p2_pos = new_pos
    p2_score = cur_score + new_pos

  if cur_score + new_pos >= 21:
    if cur_player == 1:
      DP[p1_pos][p2_pos][p1_score][p2_score][0] = 1
    else:
      DP[p1_pos][p2_pos][p1_score][p2_score][1] = 1
    return DP[p1_pos][p2_pos][p1_score][p2_score]
  
  p1, p2 = 0, 0

  for total, count in SUMS.items():
    x, y = recurse(p1_pos, p2_pos, p1_score, p2_score , total, 3 - cur_player)
    p1 += x * count
    p2 += y * count

  return [p1, p2]


def part_two():
  game = {}
  for line in sys.stdin:
    parts = line.strip().split()
    game[int(parts[1])] = {
      "pos": int(parts[-1]),
      "score": 0,
    }

  p1, p2 = 0, 0
  for total, count in SUMS.items():
    x, y = recurse(game[1]["pos"], game[2]["pos"], 0, 0, total, 1)
    p1 += x * count
    p2 += y * count

  print(max(p1, p2))

  
if __name__ == "__main__":
  part_two()
