import sys

def main(window_size):
  nums = [int(line) for line in sys.stdin]
  windows = []
  for i in range(window_size, len(nums) + 1):
    start = i - window_size
    end = i
    windows.append(sum(nums[start:end]))

  count = 0
  for i in range(1, len(windows)):
    count = count + 1 if windows[i] > windows[i-1] else count
  print(count)

if __name__ == "__main__":
  main(3)
