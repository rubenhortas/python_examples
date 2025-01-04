import copy


def sort(lst: list) -> list:
    # Complexity: O(n*log(n))
    # Auxiliary space: O(n)

    if len(lst) <= 1:
        return lst

    lst_ = copy.deepcopy(lst)

    pivot = lst_[len(lst_) // 2]
    left = [x for x in lst_ if x < pivot]
    middle = [x for x in lst_ if x == pivot]
    right = [x for x in lst_ if x > pivot]

    return sort(left) + middle + sort(right)
