from app.constants import EntitySize
from app.interfaces.parking_lot import ParkingLot
from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.parking_strategy import ParkingStrategy
from app.interfaces.vehicle import Vehicle


class GenericParkingStrategy(ParkingStrategy):

    def find_spot_for_size(self, parking_lot: ParkingLot, size: EntitySize):
        for floor in parking_lot.floors:
            for spot in floor.spots:
                if not spot.vehicle and spot.size.value >= size.value:
                    return spot

    def find_spot(self, parking_lot: ParkingLot, vehicle: Vehicle) -> ParkingSpot:
        sizes = [
            EntitySize.SMALL, EntitySize.MEDIUM, EntitySize.LARGE, EntitySize.XLARGE
        ]
        for size in sizes:
            if vehicle.size.value <= size.value:
                spot = self.find_spot_for_size(parking_lot, size)
                if spot:
                    return spot
        raise Exception('No parking spot available')