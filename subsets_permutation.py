def subset(items):
    result = []
    if not items:
        result.append([])
        return result
    previous = subset(items[:-1])
    result.extend(previous)

    for item in previous:
        new_item = item.copy()
        new_item.append(items[-1])
        result.append(new_item)

    return result


def permutaions(items):
    if not items:
        return [[]]
    previous = permutaions(items[:-1])
    result = []

    for item in previous:
        if not item:
            new_item = item.copy()
            new_item.append(items[-1])
            result.append(new_item)
        else:
            for i in range(len(item)+1):
                new_item = item.copy()
                new_item.insert(i, items[-1])
                result.append(new_item)
    return result


def main():
    print(subset([1, 2, 3]))
    print(permutaions([1, 2, 3]))


if __name__ == "__main__":
    main()
