from datetime import date


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def age(self):
        return self.calculate_age(self.birthday)

    @staticmethod
    def calculate_age(birthday):
        bday, bmonth, byear = birthday.split(".")
        bday = int(bday)
        bmonth = int(bmonth)
        byear = int(byear)
        today = date.today()
        return (today.year - byear) - ((today.month, today.day) < (bmonth, bday))


def test_person():
    print(Person.calculate_age("20.02.1975"))


class ODESolver:
    @staticmethod
    def default_parameters():
        return dict(
            scheme="BackwardEuler", max_dt=0.1, init_dt=0.01, adaptive_stepping=False
        )


if __name__ == "__main__":
    test_person()
