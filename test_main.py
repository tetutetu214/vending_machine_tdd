from main import VendingMachine

def test_initial_balance_is_zero():
    """自動販売機の初期残高は0円であることをテスト"""
    machine = VendingMachine()
    # 「machine.get_balance() == 0」がFalseならエラー
    assert machine.get_balance() == 0

def test_insert_coin():
    """コインを投入すると残高が増えることをテスト"""
    machine = VendingMachine()
    machine.insert_coin(100)
    # 「machine.get_balance() == 100」がFalseならエラー
    assert machine.get_balance() == 100

def test_get_products():
    """商品リストを取得できることをテスト"""
    machine = VendingMachine()
    products = machine.get_products()
    # isinstance組込関数(products が list型)でなければエラー
    assert isinstance(products, list)
    # len組込関数(products) が 0 より小さければエラー
    assert len(products) > 0

    # 商品の構造をチェック
    for product in products:
        # products の中に "id"がなければエラー
        assert "id" in product
        # products の中に "name"がなければエラー
        assert "name" in product
        # products の中に "price"がなければエラー
        assert "price" in product

def test_purchase_success():
    """商品を購入できることをテスト"""
    machine = VendingMachine()
    # get_products関数から商品リスト取得
    products = machine.get_products()
    # 商品リストの[0]を選択
    product = products[0]
    # 500円を入れる
    machine.insert_coin(500)
    # 商品リスト[0]の[id]を渡す
    result = machine.purchase(product["id"])
    # [id]が渡されなければエラー
    assert result["success"] is True
    # [id]が辞書型でなければエラー
    assert result["product"] == product
    # get_balance() と 500-(商品の金額)が同じでなければエラー
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
