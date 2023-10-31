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


class satellite_total_column_water_vapour_land_ocean(Main):
    name = "EO:ECMWF:DAT:SATELLITE_TOTAL_COLUMN_WATER_VAPOUR_LAND_OCEAN"
    dataset = "EO:ECMWF:DAT:SATELLITE_TOTAL_COLUMN_WATER_VAPOUR_LAND_OCEAN"

    choices = [
        "horizontal_aggregation",
        "variable",
        "format_",
    ]

    string_selects = [
        "month",
        "year",
    ]

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
        "year",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "horizontal_aggregation",
        [
            "0_05_x_0_05",
            "0_5_x_0_5",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    @normalize(
        "variable",
        [
            "all",
        ],
    )
    def __init__(
        self,
        month,
        year,
        horizontal_aggregation=None,
        format_=None,
        variable="all",
    ):
        super().__init__(
            month=month,
            year=year,
            horizontal_aggregation=horizontal_aggregation,
            format_=format_,
            variable=variable,
        )
