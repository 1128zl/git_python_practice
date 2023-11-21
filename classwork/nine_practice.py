#用户创建多个实例


'''
class User:

    def __init__(self, first_name, last_name, age, sex,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts=login_attempts

    def describe_user(self):
        print(f"first_name: {self.first_name}\n")
        print(f"last_name: {self.last_name}\n")
        print(f"age: {self.age}\n")
        print(f"sex: {self.sex}\n")
        print(f"login_attempts: {self.login_attempts}\n")

    def greet_user(self):
        print(f"Hello, {self.last_name} {self.first_name}\n")

    def increment_number_served(self,amount):
        self.login_attempts=self.login_attempts+amount
        
    def reset_login_attempts(self,amount):
        self.login_attempts=amount
        
# 创建用户对象
user1 = User("华", "李", 18, "女",0)
user2 = User("三", "张", 20, "男",0)
user3 = User("四", "赵", 22, "男",0)

# 调用对象的方法
user1.describe_user()
user1.greet_user()
user1.increment_number_served(1)
print(f"user1 login_attempts: {user1.login_attempts}\n")

user1.increment_number_served(1)
print(f"user1 login_attempts: {user1.login_attempts}\n")

user1.increment_number_served(1)
print(f"user1 login_attempts: {user1.login_attempts}\n")

user1.reset_login_attempts(0)
print(f"user1 login_attempts: {user1.login_attempts}\n")
'''


'''
user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
'''

#电池升级

'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWH battery.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

    def get_range(self):
        if self.battery_size == 40:
            range_ = 150
        elif self.battery_size == 65:
            range_ = 225
        print(f"This car can go about {range_} miles on a full charge.")


# Create an ElectricCar instance with a Battery
electric_car = ElectricCar("Nissan", "Leaf", 2024)

# Call get_range() before upgrading the battery
electric_car.battery.get_range()

# Upgrade the battery
electric_car.battery.upgrade_battery()

# Call get_range() again after upgrading the battery
electric_car.battery.get_range()

'''
#彩票
'''
import random
list=[2,'a',6,'f',9,'g',1,3,5,'t',4,7,0,'o',8]
select=random.sample(list,4)
print(f"If your choice is like to this choice,you will get the prize.")
'''
