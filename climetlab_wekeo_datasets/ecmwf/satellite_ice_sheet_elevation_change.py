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


class satellite_ice_sheet_elevation_change(Main):
    name = "EO:ECMWF:DAT:SATELLITE_ICE_SHEET_ELEVATION_CHANGE"
    dataset = "EO:ECMWF:DAT:SATELLITE_ICE_SHEET_ELEVATION_CHANGE"

    choices = [
        "version",
        "variable",
        "format_",
    ]

    string_selects = [
        "climate_data_record_type",
        "domain",
    ]

    @normalize(
        "climate_data_record_type",
        [
            "icdr",
            "tcdr",
        ],
        multiple=True,
    )
    @normalize(
        "domain",
        [
            "antarctica",
            "greenland",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "2_0",
            "3_0",
            "4_0",
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
        climate_data_record_type,
        domain,
        version=None,
        format_=None,
        variable="all",
    ):
        super().__init__(
            climate_data_record_type=climate_data_record_type,
            domain=domain,
            version=version,
            format_=format_,
            variable=variable,
        )
