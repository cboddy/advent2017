def read_input():
    with open('input.txt') as f:
        return f.read()


def run(jumps, get_next_jump_func):
    """
    Parameters
    ----------
    jumps: list[int]
    get_next_jump_func: int -> int
    """
    idx, n_step = 0, 0

    try:
        while True:
            next_idx = idx + jumps[idx]
            jumps[idx] = get_next_jump_func(jumps[idx])
            n_step += 1
            idx = next_idx
    except IndexError:
        print n_step


def main():
    _input = read_input()
    jumps = [int(line)
             for line in _input.split('\n')
             if len(line) > 0]
    # pt1
    run(list(jumps), lambda x: x + 1)
    # pt2
    run(list(jumps), lambda x: x + (-1 if x > 2 else 1))

if __name__ == '__main__':
    main()
