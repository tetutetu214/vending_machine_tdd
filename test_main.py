import main

def test_initial_balance_is_zero():
    """自動販売機の初期残高は0円であることをテスト"""
    machine = VendingMachine()
    assert machine.get_balance() == 0

def test_insert_coin():
    """コインを投入すると残高が増えることをテスト"""
    machine = VendingMachine()
    machine.insert_coin(100)
    assert machine.get_balance() == 100
