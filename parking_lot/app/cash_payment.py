from app.interfaces.payment import Payment


class CashPayment(Payment):
    def __init__(self, charge: int):
        self._charge = charge

    @property
    def charge(self) -> int:
        return self._charge