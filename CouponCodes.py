class CouponCodes:
    def __init__(self, cart_total, base_price, shipping_cost):
        self.cart_total = cart_total
        self.base_price = base_price
        self.shipping_cost = shipping_cost
        
    def calculate_best_price(self.cart_total, self.shipping_cost):
        float_cart_total = float(self.cart_total)
        percent_discount = self.base_price - self.base_price * .15
        fixed_discount = self.base_price - 12
        best_price = round(min(percent_discount, fixed_discount)+self.shipping_cost,2)
        return(" Your best price + " + str(best_price))
    #finished part 3