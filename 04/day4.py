import sys


class Board(object):
  def __init__(self):
    self.board = []
    self.evaluation = [[False for i in range(5)] for j in range(5)]
    self.total_sum = 0
    self.won = False

  def add_row(self, s):
    nums = map(int, [x for x in s.strip().split(" ") if len(x) > 0])
    self.total_sum += sum(nums)
    self.board.append(nums)

  def check(self, num):
    found = False
    for i, row in enumerate(self.board):
      for j, cell in enumerate(row):
        if cell == num:
          self.evaluation[i][j] = True
          self.total_sum -= num
          found = True
          break
      if found:
        break

    if found:
      # Check all rows.
      for row in self.evaluation:
        all_true = True
        for cell in row:
          all_true = all_true and cell
        if all_true:
          self.won = True

      # Check all columns.
      for i in range(len(self.evaluation)):
        all_true = True
        for j in range(len(self.evaluation[0])):
          all_true = all_true and self.evaluation[j][i]
        if all_true:
          self.won = True

def main():
  order = []
  boards = []
  for line in sys.stdin:
    if not order:
      order = map(int, line.strip().split(","))
      continue
    if not line.strip():
      boards.append(Board())
    else:
      boards[-1].add_row(line)

  solved = False
  for num in order:
    for board in boards:
      if not board.won:
        board.check(num)
        if board.won:
          # Is this the first board to be solved?
          if not solved:
            print(board.total_sum * num)
            solved = True

          # Is this the last board to be solved?
          is_last = True
          for b in boards:
            if not b.won:
              is_last = False
              break
          if is_last:
            print(board.total_sum * num)
            return


if __name__ == "__main__":
  main()
