#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.mercator.main import Main

LAYERS = [
    "dataset-topaz6-arc-15min-3km-be_202003",  # noqa: E501 dataset-topaz6-arc-15min-3km-be_202003
]


class arctic_analysisforecast_phy_tide(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_TIDE_002_015"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_TIDE_002_015"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "latitude",
            "longitude",
            "model_depth",
            "stereographic",
            "time",
            "vxo",
            "vyo",
            "x",
            "y",
            "zos",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="dataset-topaz6-arc-15min-3km-be_202003",
        max_date="2024-05-14T23:45:00Z",
        min_date="2018-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "dataset-topaz6-arc-15min-3km-be_202003":
            if min_date is None:
                min_date = "2018-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-14T23:45:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
