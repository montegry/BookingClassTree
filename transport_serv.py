from hotel import Hotel
from driver import Driver
from booking import Booking
import datetime


class TransportServices:
    def __init__(self):
        self._drivers = []
        self._hotels = []
        self._bookings = []

    def searchHotel(self, hotel_name):
        for i in self.hotels:
            if hotel_name == i.name:
                return i
        return None

    def searchDriver(self, name, vehNo):
        for i in self._drivers:
            if name == i.name or vehNo == i.vehNo:
                return i
        return None

    def searchBooking(self, datetimeOfPickup, fromAirport, name):
        for i in self._bookings:
            if datetimeOfPickup == i.datetimeOfPickup or fromAirport == i.fromAirport or name == i.hotel.name:
                return i
        return None

    def addHotel(self, hotel):
        if hotel not in self._hotels:
            self._hotels.append(hotel)

    def addDriver(self, driver):
        if driver not in self._drivers:
            self._drivers.append(driver)

    def addBooking(self, booking):
        if booking not in self._bookings:
            self._bookings.append(booking)

    def removeDriver(self, name, contact):
        for i in self._drivers:
            if name == i.name or contact == i.vehNo:
                self._drivers.remove(i)

    def removeBooking(self, datetimeOfPickup, fromAirport, name):
        for i in self._bookings:
            if datetimeOfPickup == i.datetimeOfPickup or fromAirport == i.fromAirport or name == i.hotel.name:
                self._bookings.remove(i)

    def assignDriver(self, datetimeOfPickup, fromAirport, hotelname, drivername, vehNo):
        driver_to_assign = ''
        booking_to_assign = ''
        for i in self._bookings:
            if datetimeOfPickup == i.datetimeOfPickup or fromAirport == i.fromAirport or hotelname == i.hotel.name:
                booking_to_assign = i
        for i in self._drivers:
            if drivername == i.name or vehNo == i.vehNo:
                driver_to_assign = i
        booking_to_assign.driver = driver_to_assign

    def hotelsStr(self):
        out_str = ''
        for i in self._hotels:
            out_str += str(i)+'\n'
        return out_str

    def driversStr(self):
        out_str = ''
        for i in self._drivers:
            out_str += str(i)+'\n'
        return out_str

    def bookingsStr(self):
        out_str = ''
        for i in self._bookings:
            out_str += str(i)+'\n'
        return out_str


if __name__ == '__main__':
    t_service_0 = TransportServices()
    drivers = {"Alan": "A1111", "Betty": "B2222", "Charlie": "C3333"}
    for item in drivers:
        t_service_0.addDriver(Driver(item, drivers[item]))
    hotels = {'Zenite': 'One  Road P111', 'Young  Lodge': '2,  Two  Road  P222'}
    for item in hotels:
        t_service_0.addHotel(Hotel(item, hotels[item]))
    for i in range(2):
        t_service_0.addBooking(Booking(datetime.datetime(2019, 12, i+1, 12-int(3**i), 45), True,
                                       t_service_0._hotels[0], 4-int(3*i)))
    print(t_service_0.bookingsStr())
    print(t_service_0.hotelsStr())
    print(t_service_0.driversStr())