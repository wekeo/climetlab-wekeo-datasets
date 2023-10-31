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


class satellite_total_column_water_vapour_ocean(Main):
    name = "EO:ECMWF:DAT:SATELLITE_TOTAL_COLUMN_WATER_VAPOUR_OCEAN"
    dataset = "EO:ECMWF:DAT:SATELLITE_TOTAL_COLUMN_WATER_VAPOUR_OCEAN"

    choices = [
        "origin",
        "climate_data_record_type",
        "temporal_aggregation",
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
        "origin",
        [
            "c3s",
            "eumetsat",
        ],
    )
    @normalize(
        "climate_data_record_type",
        [
            "icdr",
            "tcdr",
        ],
    )
    @normalize(
        "temporal_aggregation",
        [
            "6_hourly",
            "monthly",
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
        origin=None,
        climate_data_record_type=None,
        temporal_aggregation=None,
        format_=None,
        variable="all",
    ):
        super().__init__(
            month=month,
            year=year,
            origin=origin,
            climate_data_record_type=climate_data_record_type,
            temporal_aggregation=temporal_aggregation,
            format_=format_,
            variable=variable,
        )
