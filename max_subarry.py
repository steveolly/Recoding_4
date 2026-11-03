def max_subarray_brute(nums):
    if len(nums) == 1:
        return f"""sum {nums[0]}, indices ({0}, {0})"""
    first = 0
    second = 0
    high_sum = nums[first]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            total = 0
            for index in range(i, j):
                total += nums[index]
            if total > high_sum:
                high_sum = total
                first = i
                second = j-1
    return f"""sum {high_sum}, indices ({first}, {second})"""


def max_subarray_fast(nums):
    if not nums:
        return f"""sum {nums[0]}, indices ({0}, {0})"""

    current_sum = nums[0]
    high_sum = nums[0]
    first, second = 0, 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            if high_sum < nums[i]:
                first = i
        else:
            current_sum += nums[i]

        if current_sum > high_sum:
            high_sum = current_sum
            second = i
    return f"""sum {high_sum}, indices ({first}, {second})"""


def main():
    print(max_subarray_fast([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray_fast([5]))
    print(max_subarray_fast([-3, -1, -2]))


if __name__ == "__main__":
    main()
