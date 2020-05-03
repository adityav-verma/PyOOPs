## Components

- Parking Lot
    - Parking Floors
        - Parking Spots
            - Can be empty or have a vehicle (car, motorcycle, big car)
            - Type (Car, motorcyle, big car)
            - relationships on which size can hold what
    - limits of floors and spots?

- Ticket

- Payment

- Vehicle
    - type
    - registration_number
    
    
## Flows:
- A car comes to park at the parking lot
    - Parking lot will check if spot available (strategy)
    - Give a parking spot
        - Issue a ticket, which contains the parking spot and start time, car reference
    - return error if no spot available


- A car logs out of the parking lot
    - Hands the ticket
    - Price calculation (strategy)
    - Payment (contains a ticket, and mode of payment)
    - Free the spot


      