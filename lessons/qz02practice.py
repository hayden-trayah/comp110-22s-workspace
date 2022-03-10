def odd_and_even(a: list[int]) -> list[int]:
    output_list: list[int] = []
    i: int = 0
    for x in a:
        i += 1
        if x % 2 == 1 and i % 2 != 0:
            output_list.append(x)
    return output_list


print(odd_and_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
