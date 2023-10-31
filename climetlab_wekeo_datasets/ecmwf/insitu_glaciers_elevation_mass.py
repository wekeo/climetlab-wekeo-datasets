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


class insitu_glaciers_elevation_mass(Main):
    name = "EO:ECMWF:DAT:INSITU_GLACIERS_ELEVATION_MASS"
    dataset = "EO:ECMWF:DAT:INSITU_GLACIERS_ELEVATION_MASS"

    choices = [
        "variable",
        "format_",
    ]

    string_selects = [
        "file_version",
        "product_type",
    ]

    @normalize(
        "file_version",
        [
            "20170405",
            "20171004",
            "20180601",
            "20181103",
            "20191202",
            "20200824",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "elevation_change",
            "mass_balance",
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
        file_version,
        product_type,
        format_=None,
        variable="all",
    ):
        super().__init__(
            file_version=file_version,
            product_type=product_type,
            format_=format_,
            variable=variable,
        )
