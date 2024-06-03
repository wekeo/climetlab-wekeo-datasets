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

    @normalize(
        "climate_data_record_type",
        [
            "icdr",
            "tcdr",
        ],
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
            "c3s",
            "eumetsat",
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
        climate_data_record_type,
        month,
        origin,
        temporal_aggregation,
        year,
        variable="all",
        format_=None,
        limit=None,
    ):
        super().__init__(
            climate_data_record_type=climate_data_record_type,
            month=month,
            origin=origin,
            temporal_aggregation=temporal_aggregation,
            year=year,
            variable=variable,
            format_=format_,
            limit=limit,
        )
