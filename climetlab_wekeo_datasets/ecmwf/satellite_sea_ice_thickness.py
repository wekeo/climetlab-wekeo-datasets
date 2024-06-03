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


class satellite_sea_ice_thickness(Main):
    name = "EO:ECMWF:DAT:SATELLITE_SEA_ICE_THICKNESS"
    dataset = "EO:ECMWF:DAT:SATELLITE_SEA_ICE_THICKNESS"

    @normalize(
        "cdr_type",
        [
            "cdr",
            "icdr",
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
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "satellite",
        [
            "cryosat_2",
            "envisat",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1_0",
            "2_0",
            "3_0",
        ],
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
        month,
        satellite,
        version,
        year,
        variable="all",
        format_=None,
        limit=None,
    ):
        super().__init__(
            cdr_type=cdr_type,
            month=month,
            satellite=satellite,
            version=version,
            year=year,
            variable=variable,
            format_=format_,
            limit=limit,
        )
