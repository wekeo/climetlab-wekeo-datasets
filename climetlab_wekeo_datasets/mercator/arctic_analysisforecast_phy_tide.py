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
    "dataset-topaz6-arc-15min-3km-be_202003",  # noqa: E501 Arctic ocean physics analysis and forecast, 3 km quarter-hourly instantaneous (dataset-topaz6-tide-arc-qhr-myoceanv2-be)
]


class arctic_analysisforecast_phy_tide(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_TIDE_002_015"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_TIDE_002_015"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
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
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="dataset-topaz6-arc-15min-3km-be_202003",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "dataset-topaz6-arc-15min-3km-be_202003":
            if start is None:
                start = "2018-01-01T00:00:00Z"

            if end is None:
                end = "2023-09-25T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
