
from parking_space import ParkingSpace

if __name__ == "__main__":
    parking_lot = ParkingSpace()
    print(parking_lot.assign_slot("ABC123"))
    print(parking_lot.assign_slot("HJHJK124"))
    print(parking_lot.assign_slot("POA390"))