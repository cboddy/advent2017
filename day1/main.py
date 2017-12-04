def read_input():
    with open('input.txt') as f:
        return f.read()


def main():
    _input = read_input().replace('\n', '')
    print sum(int(l)
              for (l, r) in zip(_input, _input[1:] + _input[0])
              if l == r)


if __name__ == '__main__':
    main()
