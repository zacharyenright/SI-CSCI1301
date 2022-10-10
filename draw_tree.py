def draw_tree(height, char="*"):
    x = 1
    for i in range(height):
        print(" " * height, str(char) * x, " " * height)
        x += 2
        height -= 1

draw_tree(5, '$')
