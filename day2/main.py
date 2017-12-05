def read_input():
    with open('input.txt') as f:
        return f.read()


def checksum_pt1(nums):
    return max(nums) - min(nums)


def divisible_pt2(nums):
    nums = sorted(nums)
    for l_num in nums:
        for r_num in nums:
            if l_num <= r_num:
                break
            if (l_num % r_num) == 0:
                return l_num / r_num
    raise Exception('No divisible pair in {}'.format(nums))


def main():
    _input = read_input()
    num_lists = [[int(num) for num in line.split()]
                 for line in _input.split('\n')
                 if len(line)]

    # pt1
    print sum(checksum_pt1(nums)
              for nums in num_lists)
    
    # pt2
    print sum(divisible_pt2(nums)
              for nums in num_lists)


if __name__ == '__main__':
    main()
