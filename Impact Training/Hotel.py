class Customer:
    counter = 1000
    
    def __init__(self, name, address, no_of_days):
        self.customer_id = Customer.counter + 1
        Customer.counter += 1
        self.name = name
        self.address = address
        self.no_of_days = no_of_days
    
    def set_customer_name(self, name):
        self.name = name
    
    def set_address(self, address):
        self.address = address
    
    def set_no_of_days(self, no_of_days):
        self.no_of_days = no_of_days
    
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    
    def get_customer_id(self):
        return self.customer_id
    
    def get_customer_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_no_of_days(self):
        return self.no_of_days

class Room:
    counter = 100
    
    def __init__(self, price):
        Room.counter += 1
        self.room_id = None
        self.price = price
        self.customer = None
    
    def get_room_id(self):
        return self.room_id
    
    def get_price(self):
        return self.price
    
    def get_customer(self):
        return self.customer
    
    def set_room_id(self, room_id):
        self.room_id = room_id
    
    def set_price(self, price):
        self.price = price
    
    def set_customer(self, customer):
        self.customer = customer
    
    def assign_customer(self, customer):
        self.customer = customer
    
    def release_customer(self):
        self.customer = None
    
    def calculate_room_rent(self, no_of_days):
        pass

class LuxuryRoom(Room):
    def __init__(self, price=5000):
        super().__init__(price)
        self.room_id = f"L{Room.counter}"
        self.free_wifi = True
    
    def get_free_wifi(self):
        return self.free_wifi
    
    def set_free_wifi(self, free_wifi):
        self.free_wifi = free_wifi
    
    def calculate_room_rent(self, no_of_days):
        rent = self.price * no_of_days
        if no_of_days > 5:
            rent *= 0.95  # 5% discount
        return rent
    
class StandardRoom(Room):
    def __init__(self, price=3000):
        super().__init__(price)
        self.room_id = f"S{Room.counter}"
        self.comfortable_desk = True
    
    def get_comfortable_desk(self):
        return self.comfortable_desk
    
    def set_comfortable_desk(self, comfortable_desk):
        self.comfortable_desk = comfortable_desk
    
    def calculate_room_rent(self, no_of_days):
        return self.price * no_of_days

class Hotel:
    def __init__(self, room_list, location):
        self.room_list = room_list
        self.location = location
    
    def get_room_list(self):
        return self.room_list
    
    def set_room_list(self, room_list):
        self.room_list = room_list
    
    def get_location(self):
        return self.location
    
    def set_location(self, location):
        self.location = location
    
    def check_in(self, customer, room_type):
        for room in self.room_list:
            if isinstance(room, room_type) and room.get_customer() is None:
                room.assign_customer(customer)
                return True
        return False
    
    def check_out(self, customer):
        for room in self.room_list:
            if room.get_customer() == customer:
                rent = room.calculate_room_rent(customer.get_no_of_days())
                room.release_customer()
                return rent
        return False

# Testing the functionality
room_list = [LuxuryRoom() for _ in range(2)] + [StandardRoom() for _ in range(3)]
hotel = Hotel(room_list, "Vadodara")
cust1 = Customer("Aryansh", "Vadodara", 6)

if hotel.check_in(cust1, LuxuryRoom):
    print(f"Customer {cust1.get_customer_id()} checked into a Luxury Room.")
else:
    print("No Luxury Room available.")

rent = hotel.check_out(cust1)
if rent:
    print(f"Customer {cust1.get_customer_id()} checked out. Total Rent: {rent}")
else:
    print("Customer not found for checkout.")