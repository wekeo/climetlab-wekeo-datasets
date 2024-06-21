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
    "dataset-armor-3d-nrt-weekly_202012",  # noqa: E501 dataset-armor-3d-nrt-weekly
    "dataset-armor-3d-rep-monthly_202012",  # noqa: E501 dataset-armor-3d-rep-monthly
    "dataset-armor-3d-rep-weekly_202012",  # noqa: E501 dataset-armor-3d-rep-weekly
]


class multiobs_glo_phy_tsuv_3d_mynrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_TSUV_3D_MYNRT_015_012"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_TSUV_3D_MYNRT_015_012"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "mlotst",
            "so",
            "to",
            "ugo",
            "vgo",
            "zo",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-5",
            "-10",
            "-15",
            "-20",
            "-25",
            "-30",
            "-35",
            "-40",
            "-45",
            "-50",
            "-55",
            "-60",
            "-65",
            "-70",
            "-80",
            "-90",
            "-100",
            "-125",
            "-150",
            "-175",
            "-200",
            "-225",
            "-250",
            "-275",
            "-300",
            "-350",
            "-400",
            "-450",
            "-500",
            "-550",
            "-600",
            "-700",
            "-800",
            "-900",
            "-1000",
            "-1100",
            "-1200",
            "-1300",
            "-1400",
            "-1500",
            "-1750",
            "-2000",
            "-2500",
            "-3000",
            "-3500",
            "-4000",
            "-4500",
            "-5000",
            "-5500",
            "0",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-5",
            "-10",
            "-15",
            "-20",
            "-25",
            "-30",
            "-35",
            "-40",
            "-45",
            "-50",
            "-55",
            "-60",
            "-65",
            "-70",
            "-80",
            "-90",
            "-100",
            "-125",
            "-150",
            "-175",
            "-200",
            "-225",
            "-250",
            "-275",
            "-300",
            "-350",
            "-400",
            "-450",
            "-500",
            "-550",
            "-600",
            "-700",
            "-800",
            "-900",
            "-1000",
            "-1100",
            "-1200",
            "-1300",
            "-1400",
            "-1500",
            "-1750",
            "-2000",
            "-2500",
            "-3000",
            "-3500",
            "-4000",
            "-4500",
            "-5000",
            "-5500",
            "0",
        ],
    )
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        maximum_depth=None,
        minimum_depth=None,
        end_datetime="2022-12-01T00:00:00Z",
        start_datetime="1993-01-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            maximum_depth=maximum_depth,
            minimum_depth=minimum_depth,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
