# Create a function that takes a list and an int. The function should check if any 2 numbers
# within the list once added will equal the int.
# The list is guaranteed to have numbers

# [4, 2, 1, 8, 3], 9   -> True
# [4, 2, 1, 8, 3], 13   -> False
# [4, 2, 1, 8, 3], 2   -> False
# [4, 2, 1, 8, 3, 0, 1, -2], 5   -> True

def find_pair(ls, num):
    if len(ls) < 2:
        return False

    for index1 in range(len(ls)):
        for index2 in range(index1 + 1, len(ls)):
            num1 = ls[index1]
            num2 = ls[index2]
            if num1 + num2 == num:
                return True
            continue
    return False


assert (find_pair([4, 1, 2, -2], 2))  # same as unittest.assertTrue
assert not (find_pair([4, 1, 2, -2], 20))  # same as unittest.assertFalse


# [4, 2, 1, 8, 3], 9   -> True
def find_pair_faster(ls: list, num: int):
    if len(ls) < 2:
        return False
    for n in ls:
        needed = num - n
        if needed in ls:
            return True
    return False


# print(find_pair_faster([4, 2, 1, 8, 3], 9))

def find_pair_fastest(ls: list, num: int):
    if len(ls) < 2:
        return False

    my_needed_nums = {}
    for n in ls:
        needed = num - n
        if my_needed_nums.get(needed):
            return True
        my_needed_nums[n] = needed
    return False


print(find_pair_fastest([4, 2, 1, 8, 3], 9))
