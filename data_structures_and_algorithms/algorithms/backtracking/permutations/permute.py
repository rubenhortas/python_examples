def get_permutations(string: str):
    def permute(lst: list, start: int, end: int) -> None:
        def swap(i: int, j: int) -> None:
            lst[i], lst[j] = lst[j], lst[i]

        if start == end:
            permutations.append(''.join(lst))
        else:
            for i in range(start, end):
                swap(start, i)  # Swap chars

                permute(lst, start + 1, end)

                swap(start, i)  # Backtrack -> Swap back

    if not string:
        return []

    permutations = []

    permute(list(string), 0, len(string))

    return permutations
