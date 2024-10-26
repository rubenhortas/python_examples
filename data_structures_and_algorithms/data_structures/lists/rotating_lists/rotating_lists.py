# You are given a list of numbers, obtained by rotating a sorted list an unknown number of times.
# Write a function to determine the minimum number of times the original **sorted list** was rotated to obtain the given list.
# Your function should have the worst-case complexity of **O(log(n))**.
# You can assume that **all the numbers in the list are unique**.
# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] three times.

# Time complexity: O(log(n))
# Auxiliary space: O(1)
def calculate_rotations(lst: list) -> int:
    len_lst = len(lst)

    if lst:
        start = 0
        end = len_lst - 1

        while start <= end:
            mid = start + ((end - start) // 2)
            prev = (mid - 1 + len_lst) % len_lst
            next_ = (mid + 1) % len_lst

            if lst[mid] < lst[prev] and lst[mid] <= lst[next_]:
                return mid
            elif lst[mid] <= lst[end]:
                end = mid - 1
            elif lst[mid] >= lst[start]:
                start = mid + 1
        return 0
    else:
        return 0
