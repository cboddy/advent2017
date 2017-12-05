def read_input():
    with open('input.txt') as f:
        return f.read()


def get_sum_left(nums, pivot):
    return sum(l
               for (l, r) in zip(nums, nums[pivot:] + nums[:pivot])
               if l == r)


def main():
    _input = read_input().replace('\n', '')
    nums = [int(x)
            for x in _input]
    # pt1
    print get_sum_left(nums, 1)
    # pt2
    print get_sum_left(nums, len(nums) / 2)

if __name__ == '__main__':
    main()
