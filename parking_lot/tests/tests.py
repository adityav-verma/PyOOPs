import time
import unittest

from app.constants import EntitySize
from app.generic_factory import GenericFactory
from app.generic_vehicles import MotorBike, XLargeCard
from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.payment import Payment
from app.interfaces.ticket import Ticket


class TestParkingLot(unittest.TestCase):
    def setUp(self) -> None:
        factory = GenericFactory()
        parking_st = factory.create_parking_strategy()
        payment_st = factory.create_payment_strategy()
        self.parking_lot = factory.create_parking_lot(parking_st, payment_st)
        self.parking_lot.add_floor(
            factory.create_parking_floor(1, self.parking_lot)
        )
        self.parking_lot.add_floor(
            factory.create_parking_floor(2, self.parking_lot)
        )

        self.parking_lot.floors[0].add_spot(
            factory.create_parking_spot(
                1, EntitySize.SMALL, self.parking_lot.floors[0]
            )
        )
        self.parking_lot.floors[0].add_spot(
            factory.create_parking_spot(
                2, EntitySize.MEDIUM, self.parking_lot.floors[0]
            )
        )
        self.parking_lot.floors[0].add_spot(
            factory.create_parking_spot(
                2, EntitySize.XLARGE, self.parking_lot.floors[0]
            )
        )
        self.parking_lot.floors[0].add_spot(
            factory.create_parking_spot(
                2, EntitySize.XLARGE, self.parking_lot.floors[0]
            )
        )

        self.parking_lot.floors[1].add_spot(
            factory.create_parking_spot(
                1, EntitySize.SMALL, self.parking_lot.floors[1]
            )
        )
        self.parking_lot.floors[1].add_spot(
            factory.create_parking_spot(
                2, EntitySize.MEDIUM, self.parking_lot.floors[1]
            )
        )
        self.parking_lot.floors[1].add_spot(
            factory.create_parking_spot(
                2, EntitySize.XLARGE, self.parking_lot.floors[1]
            )
        )
        self.parking_lot.floors[1].add_spot(
            factory.create_parking_spot(
                2, EntitySize.XLARGE, self.parking_lot.floors[1]
            )
        )

    def test_add_vehicle_in_empty_lot(self):
        vehicle = MotorBike('1')
        ticket = self.parking_lot.park(vehicle)
        self.assertIsInstance(ticket, Ticket)
        self.assertEqual(ticket.vehicle, vehicle)
        self.assertEqual(ticket.payment, None)
        self.assertIsInstance(ticket.parking_spot, ParkingSpot)

    def test_add_vehicle_in_full_lot(self):
        for i in range(8):
            vehicle = MotorBike('1')
            self.parking_lot.park(vehicle)
        with self.assertRaises(Exception):
            self.parking_lot.park(MotorBike('1'))

    def test_add_xl_vehicle_with_full_slot(self):
        for i in range(4):
            vehicle = XLargeCard('1')
            self.parking_lot.park(vehicle)
        with self.assertRaises(Exception):
            self.parking_lot.park(XLargeCard('1'))

    def test_checkout(self):
        vehicle = MotorBike('1')
        ticket = self.parking_lot.park(vehicle)
        self.assertIsInstance(ticket, Ticket)
        self.assertEqual(ticket.vehicle, vehicle)
        self.assertEqual(ticket.payment, None)
        self.assertIsInstance(ticket.parking_spot, ParkingSpot)
        time.sleep(1)
        payment = self.parking_lot.checkout(ticket)
        self.assertIsInstance(payment, Payment)
        self.assertEqual(payment.charge, 2)

    def test_fill_checkout_park(self):
        ticket = None
        for i in range(8):
            vehicle = MotorBike('1')
            ticket = self.parking_lot.park(vehicle)
        with self.assertRaises(Exception):
            self.parking_lot.park(MotorBike('1'))
        self.parking_lot.checkout(ticket)
        vehicle = MotorBike('1')
        ticket = self.parking_lot.park(vehicle)
        self.assertIsInstance(ticket, Ticket)
        self.assertEqual(ticket.vehicle, vehicle)
        self.assertEqual(ticket.payment, None)
        self.assertIsInstance(ticket.parking_spot, ParkingSpot)

