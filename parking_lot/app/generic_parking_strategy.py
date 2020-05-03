from app.interfaces.parking_lot import ParkingLot
from app.interfaces.parking_spot import ParkingSpot
from app.interfaces.parking_strategy import ParkingStrategy
from app.interfaces.vehicle import Vehicle


class GenericParkingStrategy(ParkingStrategy):
    def find_spot(self, parking_lot: ParkingLot, vehicle: Vehicle) -> ParkingSpot:
        for floor in parking_lot.floors:
            for spot in floor.spots:
                if not spot.vehicle and spot.size.value >= vehicle.size.value:
                    return spot

        raise Exception('No parking spot available')