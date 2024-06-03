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


class sis_european_risk_flood_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_EUROPEAN_RISK_FLOOD_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_EUROPEAN_RISK_FLOOD_INDICATORS"

    @normalize(
        "city",
        [
            "amadora",
            "amersfoort",
            "antwerp",
            "athens",
            "bilbao",
            "birmingham",
            "brussels",
            "bucharest",
            "budapest",
            "frankfurt_am_main",
            "koln",
            "london",
            "milan",
            "pamplona",
            "paris",
            "prague",
            "riga",
            "rimini",
            "stockholm",
            "vienna",
        ],
        multiple=True,
    )
    @normalize(
        "dem",
        [
            "eu_dem",
            "lidar_derived",
        ],
        multiple=True,
    )
    @normalize(
        "return_period",
        [
            "10-yrs",
            "100-yrs",
            "25-yrs",
            "5-yrs",
            "50-yrs",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "expected_damage",
            "urban_depression",
            "water_depth",
            "water_mask",
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
    def __init__(self, city, dem, return_period, variable, format_=None, limit=None):
        super().__init__(
            city=city,
            dem=dem,
            return_period=return_period,
            variable=variable,
            format_=format_,
            limit=limit,
        )
