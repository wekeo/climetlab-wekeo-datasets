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


class satellite_sea_surface_temperature(Main):
    name = "EO:ECMWF:DAT:SATELLITE_SEA_SURFACE_TEMPERATURE"
    dataset = "EO:ECMWF:DAT:SATELLITE_SEA_SURFACE_TEMPERATURE"

    @normalize(
        "day",
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
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
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
        "processinglevel",
        [
            "level_3c",
            "level_4",
        ],
    )
    @normalize(
        "sensor_on_satellite",
        [
            "aatsr_on_envisat",
            "atsr1_on_ers_1",
            "atsr2_on_ers_2",
            "avhrr_on_metop_a",
            "avhrr_on_metop_b",
            "avhrr_on_noaa_07",
            "avhrr_on_noaa_09",
            "avhrr_on_noaa_11",
            "avhrr_on_noaa_12",
            "avhrr_on_noaa_14",
            "avhrr_on_noaa_15",
            "avhrr_on_noaa_16",
            "avhrr_on_noaa_17",
            "avhrr_on_noaa_18",
            "avhrr_on_noaa_19",
            "combined_product",
            "slstr_on_sentinel_3a",
            "slstr_on_sentinel_3b",
        ],
    )
    @normalize(
        "version",
        [
            "1_1",
            "2_0",
            "2_1",
        ],
    )
    @normalize(
        "year",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "all",
        ],
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
        day,
        month,
        processinglevel,
        sensor_on_satellite,
        version,
        year,
        variable="all",
        format_=None,
        limit=None,
    ):
        super().__init__(
            day=day,
            month=month,
            processinglevel=processinglevel,
            sensor_on_satellite=sensor_on_satellite,
            version=version,
            year=year,
            variable=variable,
            format_=format_,
            limit=limit,
        )
