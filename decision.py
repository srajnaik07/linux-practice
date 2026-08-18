class Robot:
	def __init__(self,name,battery):
		self.name = name
		self.battery = battery
	def show_status(self):
		print(self.name, self.battery, "%")
	def recharge(self):
		self.battery = 100
	def use_battery(self, amount):
		self.battery =self.battery - amount
	def move(self,distance):
		print(self.name," moved", distance,"meters")

rover1 = Robot("Rover1", 80)

rover1.show_status()
rover1.use_battery(30)
rover1.show_status()
rover1.move(10)
rover1.recharge()
rover1.show_status()
