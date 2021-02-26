from enum import Enum

class Functions(Enum):
    LIGHT = 0
    HORN = 1
    SMOKE = 2
    ENGINE = 3
    COACH_LIGHT = 4
    CABIN_LIGHT = 5
    PANTOGRAPH = 6

    def __repr__(self):
        return (type(self))

class TrainProperties:
    address             = 0     # address of the locomotive / consist
    max_speed           = 0     # maximum speed
    max_acceleration    = 0     # max_acceleration
    max_deceleration    = 0     # max_deceleration
    train_type          = 0     # type of train (goods, passenger, etc)
    length              = 0     # length of the train in mm

    current_speed       = 0     # speed of the train (0 - max_speed)
    current_direction   = 0     # direction of the train (1 = forward, 0 = reverse)
    wanted_speed        = 0     # desired speed
    wanted_direction    = 0     # can only be changed when speed = 0
    current_timer       = 0
    last_timer          = 0     # keep track when last checked to increment / decrement current speed according to acceleration

    # functions           = []

    def print_properties(self):
        if isinstance(self, Engine):
            print("Engine - ", end = '')
        elif isinstance(self, Consist):
            print("Consist - ", end = '')

        print(self.name, ":")
        print("  type     :", self.train_type)
        print("  address  :", self.address)
        print("  max_speed:", self.max_speed)
        print("  max_accel:", self.max_acceleration)
        print("  max_decel:", self.max_deceleration)
        print("  length   :", self.length)
        if isinstance(self, Engine) and self.consist != None:
            print("  part of:  ", self.consist.name)
        if isinstance(self, Consist) and self.engines != None:
            print("  consists of: ", end = '' )
            text = ''
            for e in self.engines:
                text += e.name + ', '
                # print(e.name, ", ", end = '' )
            for c in self.cars:
                text += c.name + ', '
                # print(c.name, ", ", end = '' )
            if len(text) > 2:
                text = text[0:-2]
            print(text)
        text = ''
        if isinstance(self, Engine):
            for f in self.engine_functions:
                text += f[0].name + ", "
        elif isinstance(self, Consist):
            for f in self.consist_functions:
                text += f.name + ", "

        text = text[: -2]
        print("  functions :", text)

    def set_speed(self, new_direction, new_speed):
        self.wanted_direction = new_direction
        self.wanted_speed = new_speed

    def update(self):
        self.current_timer += 1
        if (self.current_timer - self.last_timer) >= 1000000:
            self.last_timer = self.current_timer
            wanted_speed = self.wanted_speed if self.wanted_direction == self.current_direction else 0
            if wanted_speed > self.current_speed:
                self.current_speed += 1
            else:
                self.current_speed -= 1

            if self.current_direction != self.wanted_direction and self.current_speed == 0:
                self.current_direction = self.wanted_direction
            print(self.last_timer, self.current_timer, self.name, self.current_direction, self.current_speed)

class Engine (TrainProperties):

    def __init__(self, name, train_type, address, max_speed, acceleration, deceleration, length):
        self.name               = name
        self.train_type         = train_type
        self.address            = address
        self.max_speed          = max_speed
        self.max_acceleration   = acceleration
        self.max_deceleration   = deceleration
        self.length             = length
        self.consist            = None
        self.engine_functions   = []

    def add_function(self, function, function_number):
        self.engine_functions.append((function, function_number, 0))

    def set_function(self, function, status):
        for f in self.engine_functions:
            if f[0] == function:
                f[2] = status
                print("status changed: ", f[0], "->", f[2])


'''
    Consist properties

    A train can consist of serveral engines and cars. This we call a 'consist'. Every engine has its own
    properties. A train with one engines takes the properties of that engine. When a second engine is added
    to the train, the consist takes the 'slowest' properties of both engines to become the property for the
    consist. 
    Adding or removing engines or cars to or from the consist, will also adjust the length of the consist.


'''
class Consist(TrainProperties):

    engines             = []
    cars                = []
    consist_functions   = []
    
    def __init__( self, name, train_type, engine = None ):
        self.name               = name
        self.train_type         = train_type
        self.engines            = []
        self.cars               = []
        self.consist_functions  = []        # a list with only function codes. see class Functions
        if engine:
            self.add_engine(engine)

    def __repr__(self):
        str = self.name + ": "
        for engine in self.engines:
            str += engine.name + ", "
        for car in self.cars:
            str += car.name + ", "
        str = str[:-2]
        return str

    def add_functions(self, funcs):
        for f in funcs:
            t = f[0]
            if t not in self.consist_functions:
                self.consist_functions.append(t)

    def recalculate_properties( self ):
        self.max_speed          = 0
        self.max_acceleration   = 0
        self.max_deceleration   = 0
        self.length             = 0
        self.address            = 0
        self.consist_functions  = []
        counter = 1
        for engine in self.engines:
            if counter == 1:
                self.max_speed = engine.max_speed
                self.max_acceleration = engine.max_acceleration
                self.max_deceleration = engine.max_deceleration
                self.length = engine.length
                self.address = engine.address
                self.add_functions(engine.engine_functions)
            else:
                if engine.max_speed < self.max_speed:
                    self.max_speed = engine.max_speed
                if engine.max_acceleration < self.max_acceleration:
                    self.max_acceleration = engine.max_acceleration
                if engine.max_deceleration < self.max_deceleration:
                    self.max_deceleration = engine.max_deceleration
                self.length += engine.length
                self.add_functions(engine.functions)
            counter += 1
        for car in self.cars:
            self.length += car.length

    def add_engine(self, engine):
        if isinstance(engine, Engine):
            self.engines.append(engine)
            engine.consist = self
            self.add_functions(engine.engine_functions)
            self.recalculate_properties()
    
    def remove_engine(self, engine):
        if isinstance(engine, Engine):
            index = len(self.engines) - 1
            while index >= 0:
                # print(index)               
                if self.engines[index].name == engine.name:
                    self.engines.pop(index)
                    engine.consist = None
                index -= 1
            self.recalculate_properties()

    def add_car(self, car):
        if isinstance(car, Car):
            self.cars.append(car)
            self.length += car.length
            car.consist = self
            self.add_functions(car.car_functions)
    
    def remove_car(self, car):
        if isinstance(car, Car):
            index = len(self.cars) - 1
            while index >= 0:
                if self.cars[index].name == car.name:
                    self.cars.pop(index)
                    car.consist = None
                index -= 1
            self.recalculate_properties()

class Car:
    def __init__(self, name, car_type, length, address = 0):
        self.name = name
        self.car_type       = car_type
        self.length         = length
        self.address        = address
        self.consist        = None
        self.car_functions  = []

    def print_properties(self):
        print("Car -", self.name)
        print("  type   :", self.car_type)
        print("  length :", self.length)
        print("  address:", self.address)
        if len(self.car_functions):
            text = ''
            for f in self.car_functions:
                text += f[0].name + ", "
            text = text[:-2]
            print("  functions :", text)
            # print(self.functions)
        if self.consist:
            print("  part of:", self.consist.name)
    
    def add_function(self, function, function_number):
        self.car_functions.append((function, function_number, 0))
