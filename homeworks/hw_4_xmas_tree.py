def draw_tree(height=10, symbol='^', palindrome_numbers=False):

    """TODO
    - handle non-integer height
    - handle or support(!) non-single character values of symbol
    - support drawing multiple trees
    """
    num_branches = abs(height)
    # the widest layer of the tree
    width = num_branches*2 - 1

    # draw only if fits standard 48-line terminal
    if num_branches > 47:
        print(f'Tree of height {num_branches+1} won\'t fit in '
              f'standard 48-line terminal window. Too big to draw.')
        return

    trunk_layer = ' '*((width - 1)//2) + '|' + ' '*((width - 1)//2)
    layers = []

    for i in range(num_branches):
        """
        each layer length is an odd number,
        with the same number of symbols to the left and to the right of the symbol in the middle
        i is the number of symbols to the left and to the right of the middle
        """
        layer_width = i*2 + 1

        # width of blanks on either side of the tree at the current level
        blanks = ' ' * ((width - layer_width)//2)

        if palindrome_numbers:

            # create a list of numeric characters from 1 to 9 and then 0
            digits = []
            for j in range(1, 10):
                digits.append(str(j))
            digits.append('0')

            # build up symbols from the left end through the middle; length i+1
            left_leafage = ''

            for k in range(i+1):  # k is the position of a symbol starting from the left
                left_leafage += digits[k % 10]

            leafage = left_leafage + left_leafage[-2::-1]
        else:
            leafage = symbol * layer_width
        layer = blanks + leafage + blanks
        layers.append(layer)

    layers.append(trunk_layer)

    if height < 0:
        layers = layers[::-1]

    for item in layers:
        print(item)
    # print(trunk_layer)


draw_tree(-4, '&', [])
