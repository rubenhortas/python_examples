import copy


def sort(lst: list) -> list:
    # Time complexity: O(n^2)
    # Auxiliary space: O(1)

    if not lst:
        return []

    if len(lst) == 1:
        return lst

    lst_ = copy.deepcopy(lst)  # Create a copy of the list so as not modify the original list

    for _ in range(len(lst_) - 1):  # Repeat n-1 times
        for i in range(len(lst_) - 1):
            if lst_[i] > lst_[i + 1]:
                lst_[i], lst_[i + 1] = lst_[i + 1], lst_[i]  # Swapping

    return lst_
