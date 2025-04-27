# VendingMachineのクラス
class VendingMachine:
    # 初期化
    def __init__(self):
        self.balance = 0

    # 初期残高は0円を返す
    def get_balance(self):
        return self.balance

    # コインを投入すると残高が増える
    def insert_coin(self, amount):
        self.balance += amount
