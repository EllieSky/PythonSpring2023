#    *
#   ***
#  *****
#    |
#
#     *
#    ***
#   *****
#  *******
# *********
#     |


def make_xmas_tree(height, char):  # for a tree with height = 3
    spaces = height - 1
    for layer in range(height):
        print(' ' * (spaces-layer), char * (1 + 2*layer))
    print(' ' * spaces, '|')

make_xmas_tree(7, '1')

#    1
#   123
#  12345
# 1234567
#    |
def make_num_xmas_tree(height):
    spaces = height - 1
    for layer in range(height):
        branches = ''
        # char * (1 + 2*layer)
        # '12345'
        for n in range(1 + 2*layer):
            branches += str((n+1)%10)

        print(' ' * (spaces-layer), branches)
    print(' ' * spaces, '|')

make_num_xmas_tree(10)


# For homework:
#    1
#   121
#  12321
# 1234321
#    |

def make_palindrome_xmas_tree(height: int):
    spaces = height - 1
    for layer in range(height):
        branches = ''
        for i in range(layer + 1):
            branches += str((i + 1)%10)

        # branches += branches[layer-1::-1]
        branches += (branches[0:layer])[::-1]

        print(' ' * (spaces-layer), branches)
    print(' ' * spaces, '|')


make_palindrome_xmas_tree(11)