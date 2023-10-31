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


class ecv_for_climate_change(Main):
    name = "EO:ECMWF:DAT:ECV_FOR_CLIMATE_CHANGE"
    dataset = "EO:ECMWF:DAT:ECV_FOR_CLIMATE_CHANGE"

    choices = [
        "format_",
    ]

    string_selects = [
        "climate_reference_period",
        "month",
        "origin",
        "product_type",
        "time_aggregation",
        "variable",
        "year",
    ]

    @normalize(
        "climate_reference_period",
        [
            "1981_2010",
            "1991_2020",
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
        "origin",
        [
            "era5",
            "era_interim",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "anomaly",
            "climatology",
            "monthly_mean",
        ],
        multiple=True,
    )
    @normalize(
        "time_aggregation",
        [
            "12_month_running_mean",
            "1_month_mean",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "0_7cm_volumetric_soil_moisture",
            "precipitation",
            "sea_ice_cover",
            "surface_air_relative_humidity",
            "surface_air_temperature",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1979",
            "1980",
            "1981",
            "1982",
            "1983",
            "1984",
            "1985",
            "1986",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "2000",
            "2001",
            "2002",
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
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
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        climate_reference_period,
        month,
        origin,
        product_type,
        time_aggregation,
        variable,
        year,
        format_=None,
    ):
        super().__init__(
            climate_reference_period=climate_reference_period,
            month=month,
            origin=origin,
            product_type=product_type,
            time_aggregation=time_aggregation,
            variable=variable,
            year=year,
            format_=format_,
        )
