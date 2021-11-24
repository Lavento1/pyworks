# 배송비 계산하기
# 상품 가격이 20000원 미만이면 배송비(2500원) 포함하고
# 아니면 배송비 미포함

def get_price(unit_price, quantity):
    delivery_fee = 2500
    price = unit_price * quantity

    if price > 20000:
        return price
    else:
        return price + delivery_fee


price1 = get_price(15000, 2)
price2 = get_price(5000, 3)


print("상품 1 가격은 " + format(price2, ',d') + "원 입니다.")
# 천 단위 구분기호 : format(price2, ',d')
print("상품 2 가격은 %d원 입니다." % price2)
