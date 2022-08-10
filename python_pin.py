desired_pin = '516268'
max_tries = 3


def verify_pin(the_pin):
    return the_pin == desired_pin


def main():
    tries = 0

    while tries < max_tries:
        pin = input('please enter your pin code: ')
        if verify_pin(pin):
            print('Correct')
            break
        else:
            print('Incorrect. Please enter again: ')
        tries += 1
    else:  # Else will run when no `break` statement is run in while loop.
        print("I am LOCKIN' you out now!")


if __name__ == '__main__':
    main()
