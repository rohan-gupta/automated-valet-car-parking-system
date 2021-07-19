from app.carpark.carpark import CarPark


def test_add_lot():
    carpark = CarPark()
    for i in range(3): carpark.add_lot("Motorcycle")
    for i in range(5): carpark.add_lot("Car")
    assert len(carpark.lots["Motorcycle"]) == 3
    assert len(carpark.lots["Car"]) == 5


def test_remove_lot():
    carpark = CarPark()
    carpark.add_lot("Car")
    carpark.remove_lot("Car", 1)
    assert bool(not carpark.lots["Car"])


def test_get_vacant_lot():
    carpark = CarPark()
    for i in range(3): carpark.add_lot("Car")
    carpark.remove_lot("Car", 1)
    lot_number_vacant = carpark.get_vacant_lot("Car")
    assert lot_number_vacant == 2


def test_add_vehicle():
    carpark = CarPark()
    carpark.add_lot("Car")
    status1 = carpark.add_vehicle("car", "SGF9283P", 123456789)
    status2 = carpark.add_vehicle("car", "SGF9283P", 123456789)
    status3 = carpark.add_vehicle("car", "SGF9283Q", 123456789)
    assert status1[0] == "Accept"
    assert status2 == "Reject"
    assert status2 == "Reject"


def test_remove_vehicle():
    carpark = CarPark()
    carpark.add_lot("Car")
    status, lots = carpark.add_vehicle("car", "SGF9283P", 123456789)
    lot_type_number, parking_lot_fee = carpark.remove_vehicle("SGF9283P", 123456791)
    assert status == "Accept"
    assert lot_type_number == "CarLot1"
    assert parking_lot_fee == 2.0
    assert carpark.revenue == 2.0


def test_carpark():
    input_data = open("tests/test_data/input.txt", "r").read().splitlines()
    output_data = open("tests/test_data/output.txt", "r").read().splitlines()
    result = []
    car_lot_count, motorcycle_lot_count = map(int, input_data[0].split(" "))
    carpark = CarPark()
    for i in range(car_lot_count): carpark.add_lot("Car")
    for i in range(motorcycle_lot_count): carpark.add_lot("Motorcycle")
    for i in range(1, len(input_data)):
        command = input_data[i].split(" ")
        if command[0] == "Enter":
            status = carpark.add_vehicle(*command[1:])
        elif command[0] == "Exit":
            status = carpark.remove_vehicle(*command[1:])
        if isinstance(status, tuple):
            status = " ".join(str(item) for item in status)
        result.append(status == output_data[i-1])
    assert False not in result
