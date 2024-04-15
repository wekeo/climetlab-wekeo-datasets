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

    @normalize(
        "product_type",
        [
            "gridded",
            "hypsometry",
            "vector",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "5_0",
            "6_0",
        ],
    )
    @normalize(
        "variable",
        [
            "glacier_area",
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
        self, product_type, version, variable="glacier_area", format_=None, limit=None
    ):
        super().__init__(
            product_type=product_type,
            version=version,
            variable=variable,
            format_=format_,
            limit=limit,
        )
