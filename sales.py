def grocery_cart(my_product: dict) -> float:
    total_price = 0
    for product, price in my_product.items() :
        # total_price = total_price + price
        total_price += price
    return total_price


order = {'tomato': 30, 'thyme': 4.50, 'garlic': 7.5, 'rice': 10}

 # calling the function
total_price = grocery_cart (order)
print(total_price)