# {"JKSDJ8998":{"level":"A", "spot": 12}}
# create parking space
# find the parking spot which is empty(False)
# assign the spot to vehicle in the format {“level”: A, “spot”:19}
# change the "spot" in parking space to True
class ParkingSpace:
    def __init__(self):
        self.parked_vehicle = {}
        self.parking_lot = {"A":{}, "B":{}}
        for i in range(1,41):
            if i > 20:
                self.parking_lot["B"][i] = False
            else:
                self.parking_lot["A"][i] = False

    def find_slot(self):
        for i in range(1,41):
            if i>20 and self.parking_lot["B"][i] == False:
                return {"level":"B", "slot":i}
            elif self.parking_lot["A"][i] == False:
                return {"level":"A", "slot":i}
        return None
    
    def assign_slot(self, vehicle_number):
        available_slot = self.find_slot()
        booked_level = available_slot["level"]
        booked_slot = available_slot["slot"]
        self.parking_lot[booked_level][booked_slot] = True
        self.parked_vehicle[vehicle_number] = available_slot
        return self.parked_vehicle