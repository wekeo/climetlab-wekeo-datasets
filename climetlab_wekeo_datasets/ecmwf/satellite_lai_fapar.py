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


class satellite_lai_fapar(Main):
    name = "EO:ECMWF:DAT:SATELLITE_LAI_FAPAR"
    dataset = "EO:ECMWF:DAT:SATELLITE_LAI_FAPAR"

    choices = [
        "sensor",
        "product_version",
        "format_",
    ]

    string_selects = [
        "horizontal_resolution",
        "month",
        "nominal_day",
        "satellite",
        "variable",
        "year",
    ]

    @normalize(
        "horizontal_resolution",
        [
            "1km",
            "300m",
            "4km",
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
        "nominal_day",
        [
            "03",
            "10",
            "13",
            "20",
            "21",
            "22",
            "23",
            "24",
            "28",
            "29",
            "30",
            "31",
        ],
        multiple=True,
    )
    @normalize(
        "satellite",
        [
            "noaa_11",
            "noaa_14",
            "noaa_16",
            "noaa_17",
            "noaa_7",
            "noaa_9",
            "proba",
            "sentinel_3",
            "spot",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "fapar",
            "lai",
        ],
        multiple=True,
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
        ],
        multiple=True,
    )
    @normalize(
        "sensor",
        [
            "avhrr",
            "olci_and_slstr",
            "vgt",
        ],
    )
    @normalize(
        "product_version",
        [
            "V0",
            "V1",
            "V2",
            "V3",
            "V4",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    @normalize("area", "bounding-box(list)")
    def __init__(
        self,
        horizontal_resolution,
        month,
        nominal_day,
        satellite,
        variable,
        year,
        sensor,
        product_version,
        format_,
        area=None,
    ):
        super().__init__(
            horizontal_resolution=horizontal_resolution,
            month=month,
            nominal_day=nominal_day,
            satellite=satellite,
            variable=variable,
            year=year,
            sensor=sensor,
            product_version=product_version,
            format_=format_,
            area=area,
        )
