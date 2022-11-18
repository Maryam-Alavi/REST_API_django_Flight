from rest_framework import status
from rest_framework.test import APITestCase

from . import views
from .views import GetData


class test_data(APITestCase):

    def testDataApi(self):
        data = {"NAME_OF_FILE": "name_of_file", "COL_HEADERS": "col_headers", "COUNT_ROW": "count_row",
                "COUNT-COL": "count_col"}
        response = self.client.post("AircraftModels/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
