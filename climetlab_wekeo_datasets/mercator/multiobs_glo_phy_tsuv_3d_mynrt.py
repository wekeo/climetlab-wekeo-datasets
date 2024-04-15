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
    "dataset-armor-3d-nrt-monthly_202012",  # noqa: E501 dataset-armor-3d-nrt-monthly
    "dataset-armor-3d-nrt-monthly_202012",  # noqa: E501 Armor3d NRT - tshuvmld global ocean observation-based product monthly average
    "dataset-armor-3d-nrt-weekly_202012",  # noqa: E501 dataset-armor-3d-nrt-weekly
    "dataset-armor-3d-nrt-weekly_202012",  # noqa: E501 Armor3d NRT - tshuvmld global ocean observation-based product
    "dataset-armor-3d-rep-monthly_202012",  # noqa: E501 dataset-armor-3d-rep-monthly
    "dataset-armor-3d-rep-monthly_202012",  # noqa: E501 Armor3d rep - tshuvmld global ocean observation-based product monthly average
    "dataset-armor-3d-rep-weekly_202012",  # noqa: E501 Armor3d rep - tshuvmld global ocean observation-based product
    "dataset-armor-3d-rep-weekly_202012",  # noqa: E501 dataset-armor-3d-rep-weekly
]


class multiobs_glo_phy_tsuv_3d_mynrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_TSUV_3D_MYNRT_015_012"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_TSUV_3D_MYNRT_015_012"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "depth",
            "latitude",
            "longitude",
            "mlotst",
            "so",
            "time",
            "to",
            "ugo",
            "vgo",
            "zo",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2023-11-13T00:00:00Z",
        min_date="2020-11-06T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "dataset-armor-3d-nrt-monthly_202012":
            if min_date is None:
                min_date = "2019-01-15T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "dataset-armor-3d-nrt-weekly_202012":
            if min_date is None:
                min_date = "2020-11-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-27T00:00:00Z"

        if layer == "dataset-armor-3d-rep-monthly_202012":
            if min_date is None:
                min_date = "2020-11-06T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-13T00:00:00Z"

        if layer == "dataset-armor-3d-rep-weekly_202012":
            if min_date is None:
                min_date = "2020-10-23T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-29T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
