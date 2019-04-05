from hotel import Hotel
from driver import Driver
import datetime

class Booking:
    def __init__(self, datetimeOfPickup, fromAirport, hotel, numPassengers):
        self._hotel = hotel
        self._numPassengers = numPassengers
        self._driver = None
        self._datetimeOfPickup = datetimeOfPickup
        self._fromAirport = fromAirport

    @property
    def numPassengers(self):
        return self._numPassengers

    @property
    def driver(self):
        return self._driver

    @property
    def datetimeOfPickup(self):
        return self._datetimeOfPickup

    @property
    def from_airport(self):
        return self._fromAirport

    @datetimeOfPickup.setter
    def datatimeOfPickup(self, datetimeOfPickup):
        self._datetimeOfPickup = datetimeOfPickup

    @numPassengers.setter
    def numPassengers(self, numPassengers):
        self._numPassengers = numPassengers

    @driver.setter
    def driver(self, driver):
        self._driver = driver

    def __str__(self):
        if self._driver:
            driver = str(self.driver)
        else:
            driver = "No"
        if self._fromAirport:
            from_air = "To Hotel"
        else:
            from_air = "From Hotel"
        return "Date/time" + str(self.datetimeOfPickup) + " " + from_air + "\n\t" + str(self._hotel) + " " \
               + str(self._numPassengers) + "\n\tAssigned: " + driver


if __name__ == "__main__":
    booking_0 = Booking(datetime.datetime(2019, 12, 1, 12, 45), True, Hotel('Zenite', 'One  Road P111'), 4)
    print(booking_0.datetimeOfPickup)
    booking_0.datatimeOfPickup += datetime.timedelta(hours=1)
    print(booking_0.datetimeOfPickup)
    print(booking_0._hotel._name)
    print(str(booking_0))
