class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


Audi = SportCar(100, 'Red', 'Audi', False)
BMW = TownCar(30, 'Black', 'BMW', False)
VOLVO = WorkCar(70, 'White', 'VOLVO', True)
FORD = PoliceCar(110, 'Blue', 'FORD', True)
print(VOLVO.turn_left())
print(f'When {BMW.turn_right()}, then {Audi.stop()}')
print(f'{VOLVO.go()} with speed exactly {VOLVO.show_speed()}')
print(f'{VOLVO.name} is {VOLVO.color}')
print(f'Is {Audi.name} a police car? {Audi.is_police}')
print(f'Is {VOLVO.name}  a police car? {VOLVO.is_police}')
print(Audi.show_speed())
print(BMW.show_speed())
print(FORD.police())
print(FORD.show_speed())
