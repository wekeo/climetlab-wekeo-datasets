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
    "dataset-uv-nrt-daily",  # noqa: E501 Daily mean total surface and 15m velocities
    "dataset-uv-nrt-hourly",  # noqa: E501 Total surface and 15m velocities
    "dataset-uv-nrt-monthly",  # noqa: E501 Monthly mean total surface and 15m velocities
]


class multiobs_glo_phy_nrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_NRT_015_003"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_NRT_015_003"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "crs",
            "depth",
            "latitude",
            "longitude",
            "time",
            "uo",
            "vo",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer,
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "dataset-uv-nrt-daily":
            if start is None:
                start = "2021-07-05T00:00:00Z"

            if end is None:
                end = "2023-09-25T00:00:00Z"

        if layer == "dataset-uv-nrt-monthly":
            if start is None:
                start = "2021-07-05T00:00:00Z"

            if end is None:
                end = "2023-09-06T00:00:00Z"

        if layer == "dataset-uv-nrt-hourly":
            if start is None:
                start = "2021-07-05T00:00:00Z"

            if end is None:
                end = "2023-09-25T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
