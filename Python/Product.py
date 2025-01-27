class Product:
    def init(self , name, price,quantity):
        self.name=name
        self.price=price
        self.quantity = quantity
    def restock(self, amount):
        self.quantity+=amount
        print(f"Restocked {self.name} . new Quantity : {self.quantity}")
    def sell(self, amount):
        if amount <=self.quantity:
            self.quantity-=amount
            print(f"Sold : {amount} of {self.name}.Remaining Quantity : {self.quantity}")
        else:
            print("Not enough Stock to sell  .")
p1=Product("Laptop ", 1200 , 10)
p1.restock(5)
p1.sell(3)
p1.sell(20)