def read_input():
    with open('input.txt') as f:
        return f.read()


def pt1(jumps):
    idx, n_step = 0, 0

    try:
        while True:
            next_idx = idx + jumps[idx]
            jumps[idx] += 1
            n_step += 1
            idx = next_idx
    except IndexError:
        print n_step


def pt2(jumps):
    idx, n_step = 0, 0

    try:
        while True:
            next_idx = idx + jumps[idx]
            jumps[idx] += (-1 if jumps[idx] > 2 else 1)
            n_step += 1
            idx = next_idx
    except IndexError:
        print n_step


def main():
    _input = read_input()
    jumps = [int(line)
             for line in _input.split('\n')
             if len(line) > 0]
    pt1(list(jumps))
    pt2(list(jumps))

if __name__ == '__main__':
    main()
