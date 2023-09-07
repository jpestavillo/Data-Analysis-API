class ratioEmployees():

    def __init__(self, date, production, nonsupervisory) -> None:
        self.date = date
        self.production = production
        self.nonsupervisory = nonsupervisory
        self.supervisory = production - nonsupervisory
        self.ratio = self.production / self.supervisory

    def to_JSON(self):
        return {
            'date': self.date,
            'ratio': self.ratio
        }
