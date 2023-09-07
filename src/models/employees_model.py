from database.db import get_connection
from .entities.ratio_employees import ratioEmployees

class ratioEmployeesModel():
    @classmethod
    def get_data(self):
        try:
            connection = get_connection()
            series = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT series_id, \
                               CONCAT(TO_CHAR(TO_DATE (RIGHT(period, 2), 'MM'), 'Month'), year) as date, \
                               value AS ValueInThousands \
                               FROM employees \
                               WHERE year > 1963 \
                               AND series_id LIKE 'CES0000000001%' OR series_id like 'CES0500000006%'" )
                resultset = cursor.fetchall()
                half = len(resultset) // 2
                series = []
                for row in range(half):
                    serie = ratioEmployees(resultset[row][1], 
                                           resultset[row][2], 
                                           resultset[row + half][2]).to_JSON()
                    series.append(serie)
                connection.close()
                return series
        except Exception as ex:
            raise Exception(ex)
