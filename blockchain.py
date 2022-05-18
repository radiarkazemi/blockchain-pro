# Initializing our blockchain list
blockchain = []


def get_last_transaction_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain. 
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    user_input = float(input('Your transaction amount please: '))
    return user_input


tx_amount = get_user_input()
add_value(tx_amount)
tx_amount = get_user_input()

add_value(
    last_transaction=get_last_transaction_value(),
    transaction_amount=tx_amount)
tx_amount = get_user_input()
add_value(tx_amount, get_last_transaction_value())

print(blockchain)

# until end of part 16
