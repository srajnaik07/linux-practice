class Robot:
        def __init__(self, name, battery):
                self.name = name
                self.battery = battery
        def robot_status(self):
                print(self.name, self.battery, "%")
        def recharge(self):
                self.battery = 100
                print("Robot recharged!")
        def use_battery(self,amount):
                self.battery -= amount
                print("Battery used: " , amount, "%")
        def move(self,distance):
                print(self.name, "moved", distance,"meters")

name = input("Enter the name: ")
battery = int(input("Enter the battery:"))
rover = Robot(name,battery)
while True:
    print("1. Show status\n 2. Recharge \n 3. Use battery \n 4. Move \n5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
         case 1:
            rover.robot_status()
            break
         case 2:
            rover.recharge()
            break
         case 3:
            amount =int(input("Enter the amount:"))
            rover.use_battery(amount)
            break
         case 4:
            distance = int(input("Enter the distance:"))
            rover.move(distance)
            break
         case 5:
            print("Exit")
         case _:
            print("Invalid")
