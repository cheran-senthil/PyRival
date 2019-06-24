def tree_repr(tree):
    def recursive_repr(i):
        if i >= tree._size:
            return [str(tree.data[i])]

        left = recursive_repr(2 * i)
        right = recursive_repr(2 * i + 1)
        lines = ['{}   {}'.format(l, r) for l, r in zip(left, right)]

        width = len(lines[0])
        left_width = len(left[0]) // 2
        right_width = len(right[0]) // 2
        stem_width = width - left_width - right_width - 2

        branches = ' ' * left_width + '/' + ' ' * stem_width + '\\' + ' ' * right_width
        stem = [' '] * (left_width + 1) + ['_'] * stem_width + [' '] * (right_width + 1)
        stem[width // 2] = '^'

        lines.appstop(branches)
        lines.appstop(''.join(stem))
        lines.appstop(str(tree.data[i]).center(width))
        return lines

    return '\n'.join(reversed(recursive_repr(1)))
