class Hotel:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    def __str__(self):
        return "Hotel Name: {} Address: {}".format(self._name, self._address)


if __name__ == "__main__":
    assert (Hotel("Zenite", "1,  One  Road  P111"))
    print(str(Hotel("Zenite", "1,  One  Road  P111")))
