class Driver:
    def __init__(self, name, vehno):
        self._name = name
        self._vehNo = vehno

    @property
    def name(self):
        return self._name

    @property
    def vehno(self):
        return self._vehNo

    @vehno.setter
    def vehno(self, vehNo):
        self.vehNo = vehNo

    def __str__(self):
        return "Driver Name: {}  Vehicle number: {}".format(self.name, self._vehNo)


if __name__ == "__main__":
    assert (Driver('Alan', 'A1110'))
    driver_0 = Driver('Alan', 'A1110')
    driver_0.vehno = 'A1111'
    print(str(driver_0))
