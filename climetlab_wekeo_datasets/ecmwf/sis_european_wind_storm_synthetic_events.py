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


class sis_european_wind_storm_synthetic_events(Main):
    name = "EO:ECMWF:DAT:SIS_EUROPEAN_WIND_STORM_SYNTHETIC_EVENTS"
    dataset = "EO:ECMWF:DAT:SIS_EUROPEAN_WIND_STORM_SYNTHETIC_EVENTS"

    @normalize(
        "month",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "09",
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "version_id",
        [
            "synthetic_set_1_2",
            "synthetic_set_2_0",
            "synthetic_set_3_0",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "wind_speed_of_gusts",
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
        version_id,
        year,
        variable="wind_speed_of_gusts",
        format_=None,
        limit=None,
    ):
        super().__init__(
            month=month,
            version_id=version_id,
            year=year,
            variable=variable,
            format_=format_,
            limit=limit,
        )
