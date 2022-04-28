def feet_to_steps(user_feet):
    steps = user_feet / 2.5
    return int(steps)

if __name__ == '__main__':
    user_feet = float(input())
    print(feet_to_steps(user_feet))