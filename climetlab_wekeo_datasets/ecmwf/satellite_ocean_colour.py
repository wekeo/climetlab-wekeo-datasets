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


class satellite_ocean_colour(Main):
    name = "EO:ECMWF:DAT:SATELLITE_OCEAN_COLOUR"
    dataset = "EO:ECMWF:DAT:SATELLITE_OCEAN_COLOUR"

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
        "projection",
        [
            "regular_latitude_longitude_grid",
            "sinusoidal_grid",
        ],
    )
    @normalize(
        "variable",
        [
            "mass_concentration_of_chlorophyll_a",
            "remote_sensing_reflectance",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "4_2",
            "5_0",
            "6_0",
            "5_0_1",
        ],
    )
    @normalize(
        "year",
        [
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
            "2024",
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
        self, day, month, projection, variable, version, year, format_=None, limit=None
    ):
        super().__init__(
            day=day,
            month=month,
            projection=projection,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
            limit=limit,
        )
