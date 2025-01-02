import copy


def sort(lst: list) -> list:
    # Time complexity: O(n^2)
    # Auxiliary space: O(1)

    lst_ = copy.deepcopy(lst)  # Create a copy of the list so as not modify the original list

    for i in range(len(lst_)):
        current = lst_.pop(i)
        j = i - 1

        while j >= 0 and current < lst_[j]:
            j -= 1

        lst_.insert(j + 1, current)

    return lst_
