from app.constants import EntitySize
from app.generic_parking_floor import GenericParkingFloor
from app.generic_parking_spot import GenericParkingSpot
from app.generic_vehicles import MotorBike, Car, LargeCar, XLargeCard
from app.interfaces.factory import Factory
from app.interfaces.parking_floor import ParkingFloor
from app.interfaces.ticket import Ticket
from app.interfaces.vehicle import Vehicle


class Client:
    def __init__(self, factory: Factory):
        self._factory = factory
        parking_strategy = self._factory.create_parking_strategy()
        payment_st = self._factory.create_payment_strategy()
        self.parking_lot = self._factory.create_parking_lot(parking_strategy, payment_st)

    def add_floor(self, id):
        floor = self._factory.create_parking_floor(id, self.parking_lot)
        self.parking_lot.add_floor(floor)

    def add_spot(self, id, size: EntitySize, floor: ParkingFloor):
        spot = self._factory.create_parking_spot(id, size, floor)
        floor.add_spot(spot)

    def park(self, vehicle: Vehicle):
        try:
            ticket = self.parking_lot.park(vehicle)
            print(ticket)
            return ticket
        except Exception as e:
            print(e)

    def checkout(self, ticket: Ticket):
        payment = self.parking_lot.checkout(ticket)
        print(payment)


if __name__ == '__main__':
    client = Client()
    client.parking_lot.add_floor(GenericParkingFloor(1, client.parking_lot))
    client.parking_lot.add_floor(GenericParkingFloor(2, client.parking_lot))

    client.parking_lot.floors[0].add_spot(
        GenericParkingSpot(1, EntitySize.SMALL, client.parking_lot.floors[0])
    )
    client.parking_lot.floors[0].add_spot(
        GenericParkingSpot(2, EntitySize.MEDIUM, client.parking_lot.floors[0])
    )
    client.parking_lot.floors[0].add_spot(
        GenericParkingSpot(3, EntitySize.LARGE, client.parking_lot.floors[0])
    )
    client.parking_lot.floors[0].add_spot(
        GenericParkingSpot(4, EntitySize.XLARGE, client.parking_lot.floors[0])
    )

    bike1 = MotorBike('one')
    car1 = Car('two')
    lcar1 = LargeCar('three')
    xlcar1 = XLargeCard('four')
    xlcar2 = XLargeCard('five')


    ticket1 = client.park(bike1)
    ticket2 = client.park(car1)
    ticket3 = client.park(lcar1)
    ticket4 = client.park(xlcar1)
    client.checkout(ticket4)
    ticket5 = client.park(xlcar2)