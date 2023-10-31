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


class satellite_greenland_ice_sheet_velocity(Main):
    name = "EO:ECMWF:DAT:SATELLITE_GREENLAND_ICE_SHEET_VELOCITY"
    dataset = "EO:ECMWF:DAT:SATELLITE_GREENLAND_ICE_SHEET_VELOCITY"

    choices = [
        "variable",
        "format_",
    ]

    string_selects = [
        "period",
        "version",
    ]

    @normalize(
        "period",
        [
            "2017_2018",
            "2018_2019",
            "2019_2020",
            "2020_2021",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1.2",
            "1.3",
            "1.4",
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
    @normalize(
        "variable",
        [
            "all",
        ],
    )
    def __init__(
        self,
        period,
        version,
        format_=None,
        variable="all",
    ):
        super().__init__(
            period=period,
            version=version,
            format_=format_,
            variable=variable,
        )
