from visualiser.visualiser import Visualiser as vs

@vs(node_properties_kwargs={
    "shape": "record",
    "color": "#f57542",
    "style": "filled",
    "fillcolor": "grey"
})
def print_parens(left, right, s, n):
    print(left, right, s)
    if right == n:  # Нужно закрыть все открытые скобки
        print(s)
        return

    if left < n:
        print_parens(left + 1, right, s + "(", n)

    if right < left:
        print_parens(left, right + 1, s + ")", n)

    return s


def main(n):
    print_parens(0, 0, '', n)
    vs.make_animation("brackets.gif", delay=1)


main(3)