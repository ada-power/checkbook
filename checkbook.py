def view_current_balance():
    with open('history.txt', 'r') as f:
        transaction = f.readlines()
    current_balance = transaction[0].replace('\n','')
    return current_balance

if __name__ == '__main__':

    print('~~~ Welcome to your terminal checkbook! ~~~')

    while True:
        action = input(' What would you like to do?: ').lower().strip()
        if action == 'view':
            print(view_current_balance())



