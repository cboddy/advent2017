def read_input():
    with open('input.txt') as f:
        return f.read()


def is_valid_pt1(phrase_line):
    words = phrase_line.split()
    return len(set(words)) == len(words)


def is_valid_pt2(phrase_line):
    words = [''.join(sorted(word))
             for word in phrase_line.split()]
    return len(set(words)) == len(words)


def main():
    _input = read_input()
    lines = _input.split('\n')

    print sum(is_valid_pt1(line)
              for line in lines
              if len(line))

    print sum(is_valid_pt2(line)
              for line in lines
              if len(line))

if __name__ == '__main__':
    main()
