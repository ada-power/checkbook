def view_current_balance():
    with open('history.txt', 'r') as f:
        transaction = f.readlines()
        current_balance = transaction[0].replace('\n','')
    print('\n Your current balance is: $' + current_balance +'\n ')

def add_a_debit(debit):
    with open('history.txt', 'r') as f:
        transactions = f.read().split('\n')
    #print(transactions)
    transactions[0] = str(float(transactions[0]) - debit)
    transactions.append(f'-{debit}')
    #print(transactions)
    for i in range(len(transactions)):
        transactions[i] = transactions[i] + '\n'
    with open('history.txt', 'w') as f:
        transactions = f.write(''.join(transactions))

    view_current_balance()

def add_a_credit(credit):
    with open('history.txt', 'r') as f:
        transactions = f.read().split('\n')
    #print(transactions)
    transactions[0] = str(float(transactions[0]) + credit)
    transactions.append(f'+{credit}')
    #print(transactions)
    for i in range(len(transactions)):
        transactions[i] = transactions[i] + '\n'
    with open('history.txt', 'w') as f:
        transactions = f.write(''.join(transactions))

    view_current_balance()



if __name__ == '__main__':

    print('~~~ Welcome to your terminal checkbook! ~~~')
    print('                                           ')
    while True:
        print('What would you like to do?')
        print('--------------------------')
        print('1) view current balance')
        print('2) record a debit (withdraw)')
        print('3) record a credit (deposit)')
        print('4) view transaction history')
        print('5) exit')


        action = input('Your choice: ').lower().strip()
        while action not in ['1','2','3','4', '5']:
            print('')
            print('Invalid choice')
            action = input('Your choice: ').lower().strip()

        if action == '1' or action == 'view':
            view_current_balance()


        elif action == '5' or action == 'exit':
            break


        elif action == '2' or action == 'debit':
            debit = input('(Type "cancel" to cancel) How much is the debit?: ')
            if debit == 'cancel':
                continue
            elif debit.isdigit():
                add_a_debit(float(debit))


        elif action == '3' or action == 'credit':
            credit = input('(Type "cancel" to cancel) How much is the credit?: ')
            if credit == 'cancel':
                continue
            elif credit.isdigit():
                add_a_credit(float(credit))

        elif action == '4':
            view_transaction_history()

    print('\n~~~~ Thanks, have a great day! :) ~~~~\n')