import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying


    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self._body_whl = body_whl
        self._body_length = ''
        self._body_width = ''
        self._body_height = ''
        self.car_type = 'truck'

    body_whl = property()

    @body_whl.setter
    def body_whl(self, body_whl):
            try:
                values = gabarits.split('x')
                self._body_length = float(values[0]) if float(values[0]) > 0 else 0.0
                self._body_width = float(values[1]) if float(values[1]) > 0 else 0.0
                self._body_height = float(values[2]) if float(values[2]) > 0 else 0.0
            except Exception:
                self._body_length = 0.0
                self._body_width = 0.0
                self._body_height = 0.0


    @body_whl.getter
    def body_whl(self):
        result = str(self._body_length) + 'x' + str(self._body_width) + 'x' + str(self._body_height)
        return result


    def get_body_volume(self):
        return self._body_length * self._body_height * self._body_width








class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []
    return car_list