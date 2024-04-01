import pyinputplus as pyip


pw='hi123'
attemp = 3
while(True):
    pwInput = pyip.inputPassword('Enter Password: ')
    if pwInput == pw:
        print('\nNow enter the following info: ')
        emailInput = pyip.inputEmail('Enter Email: ')
        dateInput = pyip.inputDate('Enter Date: ')
        print('\n', emailInput, '\n', dateInput)
        break
    else:
        attemp -= 1
        print('Password incorrect!', attemp, 'Attempt(s) left!')
        if attemp == 0:
            print('\nYou are blocked from the system\n')
            break
        else: continue
