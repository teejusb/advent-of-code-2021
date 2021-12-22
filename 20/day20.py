import sys

def main():
  enhance = None
  image = []
  for line in sys.stdin:
    if enhance == None:
      enhance = line.strip()
      continue
    if not line.strip():
      continue
    image.append(list(line.strip()))

  dirs = [
    [-1,-1], [-1,0], [-1,1],
    [ 0,-1], [ 0,0], [ 0,1],
    [ 1,-1], [ 1,0], [ 1,1],
  ]
  bit = '0'

  COUNT = 50
  for c in range(COUNT):
    width = len(image[0])
    height = len(image)
    new = [['.' for _ in range(width + 2)] for _ in range(height + 2)]

    for i in range(-1, width + 1):
      for j in range(-1, height + 1):
        bin = []

        for dir in dirs:
          x = i + dir[0]
          y = j + dir[1]
          if 0 <= x and x < width and 0 <= y and y < height:
            bin.append('0' if image[x][y] == '.' else '1')
          else:
            bin.append(bit)
        new[i+1][j+1] = enhance[int("".join(bin), 2)]
    bit = '0' if enhance[int(bit*9, 2)] == '.' else '1'
    image = new

    if c == 1:
      count = 0
      for row in image:
        for c in row:
          if c == "#":
            count += 1
      print(count)

  count = 0
  for row in image:
    for c in row:
      if c == "#":
        count += 1
  print(count)
  
if __name__ == "__main__":
  main()
