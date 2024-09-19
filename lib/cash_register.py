#!/usr/bin/env python3

class CashRegister:
  pass

  def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
  def add_item(self,title,price,quantity=1):
        self.last_price = price
        self.last_title = title
        self.last_quantity = quantity
        self.total += price * quantity
        for i in range(quantity):
            self.items.append(title)
  def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")
  def void_last_transaction(self):
        self.total = self.total - (self.last_price * self.last_quantity)
        print(self.total)