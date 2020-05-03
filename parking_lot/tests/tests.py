import unittest

from app.generic_factory import GenericFactory
from client import Client


class TestParkingLot(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client(GenericFactory())
        for f in range(2):
            self.client.parking_lot.add_floor(
                self.client._factory.create_parking_floor(f, self.client.parking_lot)
            )

        for floor in self.client.parking_lot.floors:
            for s in range(2):
                floor.add_spot(self.client._factory.create_parking_spot())
