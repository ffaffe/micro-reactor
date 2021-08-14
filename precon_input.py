from time import sleep


def precon_inp():
    print('Preconditioning menu')
    print('Enter desired reactor internal temperature:')
    req_ri_temp = input()
    print('Enter desired reagent bottle (1) temperature:')
    req_bot1_temp = input()
    sleep(1.5)

    print('\nSummary')
    print('Reactor internal = {}\u2070C'.format(req_ri_temp))
    print('Reagent bottle 1 = {}\u2070C \n'.format(req_bot1_temp))
    sleep(1)

    print('''Selections confirmed
    \t\t***
Opening precondition status window
    \t\t***''')
    sleep(2)
