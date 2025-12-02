def format_input():
    with open('./input.txt', 'r') as f:
        rotations = f.readlines()

    return [rot.replace('\n', '') for rot in rotations]


def get_pw(rotations):
    def apply_rotation(rotation):
        count = int(rotation[1:])
        if rotation[0].lower() == 'l':
            count *= -1
        tempDial = dial + count
        while tempDial < 0:
            tempDial += 100
        while tempDial > 99:
            tempDial -= 100
        return tempDial
        
    pw = 0
    dial = 50
    for rotation in rotations:
        dial = apply_rotation(rotation)
        if dial == 0:
            pw += 1
    return pw

# test case
# test_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82',]
# print(get_pw(test_input))

# final input
input = format_input()
print(get_pw(input))
