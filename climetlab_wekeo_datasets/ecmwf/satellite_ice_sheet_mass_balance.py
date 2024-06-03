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


class satellite_ice_sheet_mass_balance(Main):
    name = "EO:ECMWF:DAT:SATELLITE_ICE_SHEET_MASS_BALANCE"
    dataset = "EO:ECMWF:DAT:SATELLITE_ICE_SHEET_MASS_BALANCE"

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
    def __init__(self, variable="all", format_=None, limit=None):
        super().__init__(variable=variable, format_=format_, limit=limit)
