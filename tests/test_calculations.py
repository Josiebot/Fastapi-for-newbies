from app.calculations import add, subtract, divide, multiply, BankAccount
import pytest
from app.calculations import InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.fixture
def withdraw_account():
    return BankAccount(50)



@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5), 
    (7,1, 8),
    (9, 2, 11)
])

def test_add(num1, num2, expected):
    print("testing and function")
    result= add (num1, num2)
    assert result == expected

def test_divide():
    print("testing and function")
    result= divide (6, 3)
    assert result == 2

def test_multiply():
    print("testing and function")
    result= multiply (5, 3)
    assert result == 15

def test_subtract():
    print("testing and function")
    result= subtract (5, 3)
    assert result == 2

# def test_bank_set_initial_amount():
#     bank_account = BankAccount(50)
#     print("Bank Account Balance")
#     assert bank_account.balance == 50

def test_bank_set_initial_amount(bank_account):
    print("Bank Account Balance")
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

# def test_bank_default_amount():
#     bank_account = BankAccount()
#     assert bank_account.balance == 0

def test_withdraw(withdraw_account):
    # bank_account = BankAccount(50)   
    withdraw_account.withdraw(20)
    assert withdraw_account.balance == 30
# def test_withdraw():
#     bank_account = BankAccount(50)
#     bank_account.withdraw(20)
#     assert bank_account.balance == 30

def test_deposit():
    bank_account = BankAccount(0)
    bank_account.deposit(20)
    assert bank_account.balance == 20

def test_interest(bank_account):
    # bank_account = BankAccount(50)
    bank_account.interest()
    
    assert round(bank_account.balance, 6) == 55

    # ////////////////////////////////////////////////

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (1000, 200, 800), 
    (7000,1000, 6000),
    (900, 200, 700),
    
])

def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


# def test_bank_transaction(zero_bank_account):
#     zero_bank_account.deposit(200)
#     zero_bank_account.withdraw(200)
#     assert zero_bank_account.balance == 1800

def test_insufficient_funds (bank_account): 
    with pytest.raises(Exception): 
        bank_account.withdraw (200)