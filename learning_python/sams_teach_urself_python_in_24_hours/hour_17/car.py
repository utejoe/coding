class Car(object):

    def __init__(self, make, model, transmission, color, doors=4, features = {}):
        self.make = make
        self.model = model
        self.trasnmission = transmission
        self.color = color
        self.doors = doors
        self.features = features
