def format_input():
    with open('./input.txt', 'r') as f:
        rotations = f.readlines()

    return [rot.replace('\n', '') for rot in rotations]


def get_pw(rotations):
    def apply_rotation(rotationStr):
        nonlocal pw
        rotations = int(rotationStr[1:])

        pw += rotations // 100
        rotations %= 100

        if rotationStr[0].lower() == 'l':
            rotations *= -1

        newDial = dial + rotations

        if newDial <= 0 or newDial > 99:
            if newDial < 0: 
                newDial += 100
            elif newDial > 99: 
                newDial -= 100

            if dial != 0: 
                pw += 1

        return newDial
        
    pw = 0
    dial = 50
    for rotation in rotations:
        dial = apply_rotation(rotation)

    return pw

# test case 1
# test_input1 = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82',]
# print(get_pw(test_input1))

# test case 2
# test_input2 = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R500', 'R14', 'L82',]
# print(get_pw(test_input2))

# final input
input = format_input()
print(get_pw(input))
