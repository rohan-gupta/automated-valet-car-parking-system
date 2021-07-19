from app.carpark.carpark import CarPark


carpark = CarPark()

while True:
    command = str(input()).split(" ")
    status = ""
    if command[0].isnumeric() and command[1].isnumeric():
        for i in range(int(command[0])): carpark.add_lot("Car")
        for i in range(int(command[1])): carpark.add_lot("Motorcycle")
    elif command[0] == "Enter":
        status = carpark.add_vehicle(*command[1:])
    elif command[0] == "Exit":
        status = carpark.remove_vehicle(*command[1:])
    elif command[0] == "Show":
        carpark.show_lot()
    elif command[0].title() == "Stop":
        break
    if isinstance(status, tuple):
        status = " ".join(str(item) for item in status)
    print(status)
