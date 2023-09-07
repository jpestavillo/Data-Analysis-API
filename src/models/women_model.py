from database.db import get_connection
from .entities.women_in_goverment import WomenInGoverment

class WomenInGovermentModel():
    @classmethod
    def get_data(self):
        try:
            connection = get_connection()
            series = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT series_id, \
                               CONCAT(TO_CHAR(TO_DATE (RIGHT(period, 2), 'MM'), 'Month'), year) as date, \
                               value AS ValueInThousands \
                               FROM wig \
                               WHERE series_id LIKE 'CES9000000010%'")
                resultset = cursor.fetchall()
                for row in resultset:
                    serie = WomenInGoverment(row[1], row[2]).to_JSON()
                    series.append(serie)
                connection.close()
                return series
        except Exception as ex:
            raise Exception(ex)
