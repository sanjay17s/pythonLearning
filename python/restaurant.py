class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def isOpen(self):
        return 'open'   

    def describeRes(self):
        print(f"The name of the restaurant is {self.restaurant_name}. It serves "
              f"{self.cuisine_type} food and it's {self.isOpen()}.")

momoRes = Restaurant('momo wala', 'chinese') 
momoRes.describeRes()
