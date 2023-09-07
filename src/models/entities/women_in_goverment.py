class WomenInGoverment():

    def __init__(self, date, value_in_thousands=None) -> None:
        self.date = date
        self.value_in_thousands = value_in_thousands

    def to_JSON(self):
        return {
            'date': self.date,
            'valueInThousands': self.value_in_thousands
        }
