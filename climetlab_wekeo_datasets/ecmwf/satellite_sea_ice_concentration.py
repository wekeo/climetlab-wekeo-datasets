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


class satellite_sea_ice_concentration(Main):
    name = "EO:ECMWF:DAT:SATELLITE_SEA_ICE_CONCENTRATION"
    dataset = "EO:ECMWF:DAT:SATELLITE_SEA_ICE_CONCENTRATION"

    @normalize(
        "cdr_type",
        [
            "cdr",
            "icdr",
        ],
        multiple=True,
    )
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
        "origin",
        [
            "ESA CCI",
            "EUMETSAT OSI SAF",
        ],
    )
    @normalize(
        "region",
        [
            "northern_hemisphere",
            "southern_hemisphere",
        ],
        multiple=True,
    )
    @normalize(
        "sensor",
        [
            "amsr",
            "ssmis",
        ],
    )
    @normalize(
        "temporal_aggregation",
        [
            "daily",
            "monthly",
        ],
    )
    @normalize(
        "version",
        [
            "v2",
            "v3",
        ],
    )
    @normalize(
        "year",
        [
            "1978",
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
            "2024",
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
        cdr_type,
        day,
        month,
        origin,
        region,
        sensor,
        temporal_aggregation,
        version,
        year,
        variable="all",
        format_=None,
        limit=None,
    ):
        super().__init__(
            cdr_type=cdr_type,
            day=day,
            month=month,
            origin=origin,
            region=region,
            sensor=sensor,
            temporal_aggregation=temporal_aggregation,
            version=version,
            year=year,
            variable=variable,
            format_=format_,
            limit=limit,
        )
