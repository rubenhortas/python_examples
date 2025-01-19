def sort(lst: list) -> list:
    # Time complexity: O(n*log(n))
    # Auxiliary space: O(n)

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    left_sorted = sort(left_half)
    right_sorted = sort(right_half)

    result = _merge(left_sorted, right_sorted)

    return result


def _merge(left, right) -> list:
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result
