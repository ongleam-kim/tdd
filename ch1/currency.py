# Money 클래스 - 다중 통화 지원
class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def amount(self):
        return self._amount

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        if self._currency != addend.currency():
            raise ValueError("통화가 다른 경우 더할 수 없습니다")
        return Money(self._amount + addend.amount(), self._currency)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self._amount == other.amount() and self._currency == other.currency()

    def __repr__(self):
        return f"{self._amount} {self._currency}"


# 팩토리 메서드
def dollar(amount):
    return Money(amount, "USD")


def won(amount):
    return Money(amount, "KRW")
