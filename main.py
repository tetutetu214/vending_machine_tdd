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
        self.valid_coins = [10, 50, 100, 500]
    #
    def get_balance(self):
        return self.balance
    #
    def insert_coin(self, amount):
        if amount in self.valid_coins:
            self.balance += amount
            return True
        return False
    #
    def get_products(self):
        # 配列のコピーを返す（イミュータブル）
        return self.products.copy()
    #
    def get_product_by_id(self, product_id):
        """IDから商品を取得するヘルパーメソッド"""
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None
    #
    def purchase(self, product_id):
        product = self.get_product_by_id(product_id)
        
        if product is None:
            return {
                "success": False,
                "message": "商品が見つかりません"
            }
        
        if self.balance < product["price"]:
            return {
                "success": False,
                "message": "残高不足です"
            }
        
        self.balance -= product["price"]
        
        return {
            "success": True,
            "product": product
        }