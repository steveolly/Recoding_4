def binary_search(nums, target) -> tuple[int, int]:
    if not nums:
        return (-1, 0)
    low, high, compare = 0, len(nums)-1, 0
    mid = high//2
    target_index = -1

    while low <= high:
        if nums[mid] < target:
            low = mid+1
            mid = (high + low)//2
            compare += 1
            continue
        if nums[mid] > target:
            high = mid-1
            mid = (low + mid)//2
            compare += 1
            continue
        if nums[mid] == target:
            compare += 1
            target_index = mid
            high = mid-1
            mid = (low + high)//2
            continue

    return (target_index, compare)


def main():
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9], 9))
    print(binary_search([1, 3, 3, 3, 5, 8], 3))
    print(binary_search([1, 3, 5, 8], 4))
    print(binary_search([], 7))


if __name__ == "__main__":
    main()
