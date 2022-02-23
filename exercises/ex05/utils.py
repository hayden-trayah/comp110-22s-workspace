"""Utils file used for exercise 05."""

__author__ = "730325581"


def only_evens(numbers: list[int]) -> list[int]:
    """Outputs the even integers in the list."""
    output_list: list[int] = []
    for x in numbers:
        if x % 2 == 0:
            output_list.append(x)
    return output_list
        

def sub(nums: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns the items in a list between the specified indices."""
    if len(nums) == 0 or start_index >= len(nums) or end_index <= 0:
        return []
    
    if start_index < 0:
        start_index = 0
    
    if end_index > len(nums):
        end_index = len(nums)
    output_list: list[int] = []
    i: int = 0
    for x in nums:
        if i >= start_index and i <= end_index - 1:
            output_list.append(nums[i])
        i += 1
    return output_list


def concat(int_list: list[int], int_list2: list[int]) -> list[int]:
    """Combines the two inputed lists."""
    output_list: list[int] = []
    for x in int_list:
        output_list.append(x)
    
    for x in int_list2:
        output_list.append(x)
    return output_list