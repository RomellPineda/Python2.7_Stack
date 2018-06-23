# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
# Attributes:

# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"
# Methods:

# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return Item: takes reason_for_return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been opened, set the status to "used" and apply a 20% discount.  (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product:
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"
		self.tax = 0.12
	def sold(self):
		self.status = "sold"
		print(f"this item has been {self.status}")
		return self
	def taxed(self):
		self.price = self.price + (self.price * self.tax)
		print("got taxed")
		return self
	def reason_for_return(self, reason):
		if reason == "defective":
			self.status = reason
			self.price = 0
			print("returned")
		if reason == "like_new":
			self.status = "for sale"
			print("like new")
		if reason == "opened":
			self.status = "used"
			self.price = self.price * .80
	def display_info(self):
		print(f"Price: {self.price} \nItem_name: {self.item_name} \nWeight: {self.weight} \nBrand: {self.brand} \nStatus: {self.status}")
		return self
apple = Product(.75, "apple", .25, "mac")
apple.reason_for_return("defective")
apple.display_info()
banana = Product(.80, "banana", .30, "chiquita").display_info()