#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.ecmwf.main import Main


class seasonal_postprocessed_pressure_levels(Main):
    name = "EO:ECMWF:DAT:SEASONAL_POSTPROCESSED_PRESSURE_LEVELS"
    dataset = "EO:ECMWF:DAT:SEASONAL_POSTPROCESSED_PRESSURE_LEVELS"

    choices = [
        "originating_centre",
        "system",
        "format_",
    ]

    string_selects = [
        "leadtime_month",
        "month",
        "pressure_level",
        "product_type",
        "variable",
        "year",
    ]

    @normalize(
        "leadtime_month",
        [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
        ],
        multiple=True,
    )
    @normalize(
        "month",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "pressure_level",
        [
            "10",
            "100",
            "1000",
            "200",
            "30",
            "300",
            "400",
            "50",
            "500",
            "700",
            "850",
            "925",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "ensemble_mean",
            "monthly_mean",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "geopotential_anomaly",
            "specific_humidity_anomaly",
            "temperature_anomaly",
            "u_component_of_wind_anomaly",
            "v_component_of_wind_anomaly",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "2017",
            "2018",
            "2019",
            "2020",
            "2021",
            "2022",
            "2023",
        ],
        multiple=True,
    )
    @normalize(
        "originating_centre",
        [
            "cmcc",
            "dwd",
            "eccc",
            "ecmwf",
            "jma",
            "meteo_france",
            "ncep",
            "ukmo",
        ],
    )
    @normalize(
        "system",
        [
            "1",
            "12",
            "13",
            "14",
            "15",
            "2",
            "21",
            "3",
            "35",
            "4",
            "5",
            "51",
            "6",
            "600",
            "601",
            "602",
            "7",
            "8",
        ],
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    @normalize("area", "bounding-box(list)")
    def __init__(
        self,
        leadtime_month,
        month,
        pressure_level,
        product_type,
        variable,
        year,
        originating_centre,
        system,
        format_,
        area=None,
    ):
        super().__init__(
            leadtime_month=leadtime_month,
            month=month,
            pressure_level=pressure_level,
            product_type=product_type,
            variable=variable,
            year=year,
            originating_centre=originating_centre,
            system=system,
            format_=format_,
            area=area,
        )
