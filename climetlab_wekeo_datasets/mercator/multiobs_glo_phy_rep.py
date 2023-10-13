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
    "dataset-uv-rep-daily_201912",  # noqa: E501 Daily mean total surface and 15m velocities
    "dataset-uv-rep-hourly_201912",  # noqa: E501 Total surface and 15m velocities
    "dataset-uv-rep-monthly_201912",  # noqa: E501 Monthly mean total surface and 15m velocities
]


class multiobs_glo_phy_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_REP_015_004"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_REP_015_004"

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
        if layer == "dataset-uv-rep-hourly_201912":
            if start is None:
                start = "2019-10-19T00:00:00Z"

            if end is None:
                end = "2023-05-11T00:00:00Z"

        if layer == "dataset-uv-rep-daily_201912":
            if start is None:
                start = "2019-10-19T00:00:00Z"

            if end is None:
                end = "2023-05-11T00:00:00Z"

        if layer == "dataset-uv-rep-monthly_201912":
            if start is None:
                start = "2019-11-05T00:00:00Z"

            if end is None:
                end = "2023-05-11T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
