def read_input():
    with open('input.txt') as f:
        return f.read()


def checksum(line):
    nums = [int(num)
            for num in line.split()]
    return max(nums) - min(nums)


def main():
    _input = read_input()
    print sum(checksum(line)
              for line in _input.split('\n')
              if len(line))


if __name__ == '__main__':
    main()
