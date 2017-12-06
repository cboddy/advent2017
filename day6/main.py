def read_input():
    return [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]


def redist(banks):
    """
    Parameters
    ----------
    blocks: `list[int]`
    """
    idx_max = banks.index(max(banks))
    n_banks = len(banks)
    n_blocks = banks[idx_max]
    extra = n_blocks / n_banks
    remainder = n_blocks % n_banks
    banks[idx_max] = 0
    for i in xrange(n_banks):
        idx = (idx_max + 1 + i) % n_banks
        delta = extra + (1 if i < remainder else 0)
        banks[idx] += delta


def to_hashable(banks):
    return reduce(lambda acc, x: 31 * acc + x,
                  reversed(banks))


def main():
    banks = read_input()
    print('input', banks)
    rounds = set()
    h = None
    while h not in rounds:
        rounds.add(h)
        redist(banks)
        h = to_hashable(banks)
    print(len(rounds))


if __name__ == '__main__':
    main()
