import engine

def print_movable_items():
    print()
    print("list of movable items:")
    for thing in list_of_movable_items:
        if isinstance(thing, engine.Engine):
            if thing.consist == None:
                thing.print_properties()
        elif isinstance(thing, engine.Consist):
            if len(thing.engines) > 0:
                thing.print_properties()


list_of_movable_items = []

engine1 = engine.Engine("Assen", "Passenger", 1617, 24, 5, 5, 25)
engine1.add_function(engine.Functions.LIGHT, 0)
engine1.add_function(engine.Functions.HORN, 2)
engine1.print_properties()
list_of_movable_items.append(engine1)

engine2 = engine.Engine("Groningen", "Passenger", 1638, 28, 6, 6, 15)
engine2.add_function(engine.Functions.LIGHT, 0)
list_of_movable_items.append(engine2)

engine3 = engine.Engine("Beilen", "Freight", 1310, 20, 3, 3, 30)
engine3.add_function(engine.Functions.LIGHT, 0)
engine3.add_function(engine.Functions.SMOKE, 1)
list_of_movable_items.append(engine3)

engine4 = engine.Engine("Apekop", "Passenger", 942, 28, 6, 6, 400)
engine4.add_function(engine.Functions.LIGHT, 0)
engine4.add_function(engine.Functions.CABIN_LIGHT, 3)
engine4.add_function(engine.Functions.COACH_LIGHT, 4)
engine4.add_function(engine.Functions.PANTOGRAPH, 2)
list_of_movable_items.append(engine4)

train1 = engine.Consist("Intermodal", "Goods", engine1)
list_of_movable_items.append(train1)

train2 = engine.Consist("Gn-Zw", "passenger", engine2)
list_of_movable_items.append(train2)

train3 = engine.Consist("Coal train", "Freight", engine3)
list_of_movable_items.append(train3)

mycars = []
mycars.append(engine.Car("coach1", "passenger", 150, 1234))
mycars[0].add_function(engine.Functions.COACH_LIGHT, 4)

mycars.append(engine.Car("coach2", "passenger", 150, 1235))
mycars[1].add_function(engine.Functions.COACH_LIGHT, 5)

mycars[0].print_properties()
mycars[1].print_properties()

mycars.append(engine.Car("coach3", "passenger", 150))
mycars.append(engine.Car("coach4", "passenger", 150))
mycars.append(engine.Car("coach5", "passenger", 150))
mycars.append(engine.Car("coal1", "freight", 100))
mycars.append(engine.Car("coal2", "freight", 100))
mycars.append(engine.Car("coal3", "freight", 100))
mycars.append(engine.Car("coal4", "freight", 100))
mycars.append(engine.Car("coal5", "freight", 100))
mycars.append(engine.Car("coal6", "freight", 100))



train1.add_car(mycars[0])
train1.add_car(mycars[1])
train1.add_car(mycars[2])
train2.add_car(mycars[3])
train2.add_car(mycars[4])

train3.add_car(mycars[5])
train3.add_car(mycars[6])
train3.add_car(mycars[7])
train3.add_car(mycars[8])
train3.add_car(mycars[9])
train3.add_car(mycars[10])

train1.print_properties()
train2.print_properties()
train3.print_properties()

print_movable_items()



train3.set_speed(0, 15)

while train3.current_direction != train3.wanted_direction or train3.current_speed != train3.wanted_speed:
    train3.update()
    # print(train3.current_speed)

train3.set_speed(1, 5)

while train3.current_direction != train3.wanted_direction or train3.current_speed != train3.wanted_speed:
    train3.update()