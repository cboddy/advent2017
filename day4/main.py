def read_input():
    with open('input.txt') as f:
        return f.read()


def is_valid(phrase_line):
    words = phrase_line.split()
    return len(set(words)) == len(words)


def main():
    _input = read_input()
    lines = _input.split('\n')
    print sum(is_valid(line)
              for line in lines
              if len(line))

if __name__ == '__main__':
    main()
