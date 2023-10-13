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


class insitu_glaciers_extent(Main):
    name = "EO:ECMWF:DAT:INSITU_GLACIERS_EXTENT"
    dataset = "EO:ECMWF:DAT:INSITU_GLACIERS_EXTENT"

    choices = [
        "variable",
        "format_",
    ]

    string_selects = [
        "version",
    ]

    @normalize(
        "version",
        [
            "5_0",
            "6_0",
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
        version,
        format_,
        variable="all",
    ):
        super().__init__(
            version=version,
            format_=format_,
            variable=variable,
        )
