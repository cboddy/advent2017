def manhatten_distance():
    # max, min i,j position reached on board
    min_i, max_i, min_j, max_j = 0, 0, 0, 0
    # current i,j position in plane
    curr_i, curr_j = 0, 0
    left, up, right, down = 0, 1, 2, 3
    curr_dir = 0
    yield 0
    while True:
        if curr_dir == left:
            if curr_i == max_i:
                max_i += 1
                curr_dir = (curr_dir + 1) % 4
            curr_i += 1
        elif curr_dir == up:
            if curr_j == max_j:
                max_j += 1
                curr_dir = (curr_dir + 1) % 4
            curr_j += 1
        elif curr_dir == right:
            if curr_i == min_i:
                min_i -= 1
                curr_dir = (curr_dir + 1) % 4
            curr_i -= 1
        elif curr_dir == down:
            if curr_j == min_j:
                min_j -= 1
                curr_dir = (curr_dir + 1) % 4
            curr_j -= 1

        yield abs(curr_i) + abs(curr_j)


def main():
    gen = manhatten_distance()
    for _ in range(289326):
        val = next(gen)
    print val


if __name__ == '__main__':
    main()
