# VendingMachineのクラス
class VendingMachine:
    # 初期化
    def __init__(self):
        self.balance = 0
        self.products = [
            {"id": 1, "name": "コーラ", "price": 150},
            {"id": 2, "name": "お茶", "price": 130},
            {"id": 3, "name": "水", "price": 100}
        ]

    # 初期残高は0円を返す
    def get_balance(self):
        return self.balance

    # コインを投入すると残高が増える
    def insert_coin(self, amount):
        self.balance += amount

    # 商品を返す
    def get_products(self):
        return self.products

    # 商品を購入
    def purchase(self, product_id):
        product = None
        for p in self.products:
            if p["id"] == product_id:
                product

        if product is None:
            return {
                "success": False,
                "message": "商品が見つかりません"
            }

        # 残高チェック
        if self.balance < product["price"]:
            return {
                "success": False,
                "message": "残高不足です"
            }

        # 購入処理
        self.balance -= product["price"]
        return {
            "success": True,
            "product": product
        }
