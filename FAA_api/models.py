import json
import os
from django.db import models
from fastparquet import ParquetFile
import pandas as pd


class Data(models.Model):
    pf = ParquetFile(r"faa_data\carriers.parquet")
    dataFrame = pf.to_pandas()
    name_of_file = os.path.basename(r"faa_data\carriers.parquet")
    col_headers = sorted(dataFrame)
    count_row = dataFrame.shape[0]  # Gives number of rows
    count_col = dataFrame.shape[1]  # Gives number of columns
    data = [{"NAME_OF_FILE": name_of_file, "COL_HEADERS": col_headers, "COUNT_ROW": count_row, "COUNT-COL": count_col}]

    pf = ParquetFile(r"faa_data\aircraft.parquet")
    dataFrame = pf.to_pandas()
    name_of_file = os.path.basename(r"faa_data\aircraft.parquet")
    col_headers = sorted(dataFrame)
    count_row = dataFrame.shape[0]  # Gives number of rows
    count_col = dataFrame.shape[1]  # Gives number of columns
    data2 = [{"NAME_OF_FILE": name_of_file, "COL_HEADERS": col_headers, "COUNT_ROW": count_row, "COUNT-COL": count_col}]

    pf = ParquetFile(r"faa_data\aircraft_models.parquet")
    dataFrame = pf.to_pandas()
    name_of_file = os.path.basename(r"faa_data\aircraft_models.parquet")
    col_headers = sorted(dataFrame)
    count_row = dataFrame.shape[0]  # Gives number of rows
    count_col = dataFrame.shape[1]  # Gives number of columns
    data3 = [{"NAME_OF_FILE": name_of_file, "COL_HEADERS": col_headers, "COUNT_ROW": count_row, "COUNT-COL": count_col}]

    pf = ParquetFile(r"faa_data\airports.parquet")
    dataFrame = pf.to_pandas()
    name_of_file = os.path.basename(r"faa_data\airports.parquet")
    col_headers = sorted(dataFrame)
    count_row = dataFrame.shape[0]  # Gives number of rows
    count_col = dataFrame.shape[1]  # Gives number of columns
    data4 = [{"NAME_OF_FILE": name_of_file, "COL_HEADERS": col_headers, "COUNT_ROW": count_row, "COUNT-COL": count_col}]

    pf = ParquetFile(r"faa_data\flights.parquet")
    dataFrame = pf.to_pandas()
    name_of_file = os.path.basename(r"faa_data\flights.parquet")
    col_headers = sorted(dataFrame)
    count_row = dataFrame.shape[0]  # Gives number of rows
    count_col = dataFrame.shape[1]  # Gives number of columns
    data5 = [{"NAME_OF_FILE": name_of_file, "COL_HEADERS": col_headers, "COUNT_ROW": count_row, "COUNT-COL": count_col}]

    alldata = data + data2 + data3 + data4 + data5

    def __str__(self):
        return self.dataFrame


class AircraftModels(models.Model):
    pf = ParquetFile(r"faa_data\aircraft_models.parquet")
    dataFrame = pf.to_pandas()
    needed_data = dataFrame[["model", "manufacturer", "seats"]]

    def __str__(self):
        return self.dataFrame


class ActiveAircraft(models.Model):
    pf = ParquetFile(r"faa_data\aircraft.parquet")
    dataFrame_aircraft = pf.to_pandas()
    ActiveAircafts_status = dataFrame_aircraft.loc[dataFrame_aircraft["status_code"] == "A"]
    needed_data_aircraft = ActiveAircafts_status[["name", "county"]]

    pf = ParquetFile(r"faa_data\aircraft_models.parquet")
    dataFrame_aircraft_models = pf.to_pandas()
    needed_data_aircraft_models = dataFrame_aircraft_models[["manufacturer", "model", "seats"]]

    Data = [{"needed_data_aircraft": needed_data_aircraft, "needed_data_aircraft_models": needed_data_aircraft_models}]

    def __str__(self):
        return self.dataFrame_aircraft


class ReportOfActiveUser(models.Model):
    pf = ParquetFile(r"faa_data\aircraft.parquet")
    dataFrame_aircraft = pf.to_pandas()
    ActiveAircrafts_status = dataFrame_aircraft[["name", "county"]]
    Data = [{"ActiveAircrafts_status": ActiveAircrafts_status}]

    def __str__(self):
        return self.dataFrame_aircraft


class PivotReports(models.Model):
    pf = ParquetFile(r"faa_data\aircraft.parquet")
    dataFrame_aircraft = pf.to_pandas()
    ActiveAircafts_status = dataFrame_aircraft.loc[dataFrame_aircraft["status_code"] == "A"]
    needed_data_aircraft = ActiveAircafts_status[["name", "county"]]

    pivot = needed_data_aircraft.pivot_table(index=['name'], values=['county'])
