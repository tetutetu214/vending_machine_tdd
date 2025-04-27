from main import VendingMachine

def test_initial_balance_is_zero():
    """自動販売機の初期残高は0円であることをテスト"""
    machine = VendingMachine()
    assert machine.get_balance() == 0

def test_insert_coin():
    """コインを投入すると残高が増えることをテスト"""
    machine = VendingMachine()
    machine.insert_coin(100)
    assert machine.get_balance() == 100

def test_get_products():
    """商品リストを取得できることをテスト"""
    machine = VendingMachine()
    products = machine.get_products()
    assert isinstance(products, list)
    assert len(products) > 0

    # 商品の構造をチェック
    for product in products:
        assert "id" in product
        assert "name" in product
        assert "price" in product

def test_purchase_success():
    """商品を購入できることをテスト"""
    machine = VendingMachine()
    products = machine.get_products()
    product = products[0]  # 最初の商品を選択

    # 十分なお金を入れる
    machine.insert_coin(500)
    result = machine.purchase(product["id"])
    assert result["success"] is True
    assert result["product"] == product
    assert machine.get_balance() == 500 - product["price"]

def test_purchase_insufficient_balance():
    """残高不足の場合は購入できないことをテスト"""
    machine = VendingMachine()
    products = machine.get_products()
    product = products[0]

    # わざと少ないお金を入れる
    machine.insert_coin(10)
    result = machine.purchase(product["id"])
    assert result["success"] is False
    assert result["message"] == "残高不足です"
    assert machine.get_balance() == 10  # 残高は変わらない
