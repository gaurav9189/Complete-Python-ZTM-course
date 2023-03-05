# Python bascis 2 exercise
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

picture2 = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# Converted this into a function for re-usability


def draw(picture, pixel):
    for row in picture:
        for p in row:
            if p:  # simple readability with truthy value
                print(f'{pixel}', end='')
            else:
                print(' ', end='')
        print('')  # to have a newline once the row is complete


draw(picture2, pixel='$')
