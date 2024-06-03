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


class satellite_fire_burned_area(Main):
    name = "EO:ECMWF:DAT:SATELLITE_FIRE_BURNED_AREA"
    dataset = "EO:ECMWF:DAT:SATELLITE_FIRE_BURNED_AREA"

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
            "01",
            "07",
            "22",
        ],
        multiple=True,
    )
    @normalize(
        "origin",
        [
            "c3s",
            "esa_cci",
        ],
    )
    @normalize(
        "region",
        [
            "africa",
            "asia",
            "australia",
            "europe",
            "north_america",
            "south_america",
        ],
        multiple=True,
    )
    @normalize(
        "sensor",
        [
            "modis",
            "olci",
        ],
    )
    @normalize(
        "variable",
        [
            "grid_variables",
            "pixel_variables",
        ],
    )
    @normalize(
        "version",
        [
            "1_0",
            "1_1",
            "5_0cds",
            "5_1_1cds",
            "5_1cds",
        ],
    )
    @normalize(
        "year",
        [
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
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        month,
        nominal_day,
        origin,
        region,
        sensor,
        variable,
        version,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            month=month,
            nominal_day=nominal_day,
            origin=origin,
            region=region,
            sensor=sensor,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
            limit=limit,
        )
