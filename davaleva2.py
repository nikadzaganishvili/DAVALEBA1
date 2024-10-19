import datetime


class Customer:
    def __init__(self, name, date_0f_birth: datetime.date, balance, ):
        self.name = name
        self.date_of_birth = date_0f_birth
        self.balance = balance
    @property
    def age(self) -> int:
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount


            def withdraw(self, amount: float):
                if 0 < amount <= self.balance:
                    self.balance -= amount


class Bank:
    def __init__(self, name, customers):
        self.name = name
        self.customers = []

        @property
        def budget(self) -> float:
            return sum(customer.balance for customer in self.customers)

    def add_customer(self, Customer):
        self.customers.append(Customer)

    def remove_customer(self, Customer):
        self.customers.remove(Customer)

    def get_loan(self, customers: Customer, amount: float) -> bool:
        return Customer.balance >= (amount / 2)
