import random


def roll_dice(number=3, points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while number > 0:
        point = random.randrange(1, 7)
        points.append(point)
        number -= 1
    return points


def roll_result(total):
    isbig = 11 <= total <= 18
    issmall = 3 <= total <= 10
    if isbig:
        return 'Big'
    elif issmall:
        return 'Small'


def start_game(init_money=1000):
    print('<<<<< GAME STARTS! >>>>>')
    choices = ['Big', 'Small']
    your_choice = input('Big / Small / Help / End:')
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        you_win = your_choice == roll_result(total)
        your_bet = input('How much you wanna bet ? -')
        your_bet = int(your_bet)
        your_account = init_money
        if your_bet <= init_money:
            if you_win:
                print('The points are {}, You Win !'.format(points))
                your_account += your_bet
                print('You gained ${}, you have ${} now'.format(your_bet, your_account))
                start_game(your_account)
            else:
                print('The points are {}, You Lose!'.format(points))
                your_account -= your_bet
                print('You lost ${}, you have ${} now'.format(your_bet, your_account))
                if your_account == 0:
                    print('GAME OVER')
                else:
                    start_game(your_account)
        else:
            print('Your account is ${}, less then ${}'.format(your_account,your_bet))
            start_game(your_account)
    elif your_choice == 'End':
        print('Your account is', init_money, '!\nBye!')
        return 1
    elif your_choice == 'Help':
        print('''
         >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><
         > This is a rolling dice game.                        <
         > Choose big or small before you bet.                 <
         > The default total amount in your account is $1000.  <
         > Bet at least $10 one time.                          <
         > Enter 'End' to end the game.                        <
         > Good Luck!                                          <
         <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
         ''')
        start_game(init_money)
    else:
        print('Invalid Words')
        start_game(init_money)


start_game()
