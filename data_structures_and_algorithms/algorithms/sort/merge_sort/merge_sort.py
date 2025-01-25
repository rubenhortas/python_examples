def sort(lst: list) -> list:
    # Time complexity: O(n*log(n))
    # Auxiliary space: O(n)

    def merge() -> list:
        result = []
        left_index = 0
        right_index = 0

        while left_index < len(left_sorted) and right_index < len(right_sorted):
            if left_sorted[left_index] <= right_sorted[right_index]:
                result.append(left_sorted[left_index])
                left_index += 1
            else:
                result.append(right_sorted[right_index])
                right_index += 1

        result.extend(left_sorted[left_index:])
        result.extend(right_sorted[right_index:])

        return result

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    left_sorted = sort(left_half)
    right_sorted = sort(right_half)

    return merge()
