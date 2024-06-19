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
    "cmems_obs_glo_bgc3d_rep_weekly_202112",  # noqa: E501 cmems_obs_glo_bgc3d_rep_weekly
]


class multiobs_glo_bio_bgc_3d_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_BIO_BGC_3D_REP_015_010"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_BIO_BGC_3D_REP_015_010"

    @normalize(
        "variables",
        [
            "bbp",
            "bbp_error",
            "chl",
            "chl_error",
            "poc",
            "poc_error",
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
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
            "0",
        ],
    )
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        variables,
        layer="cmems_obs_glo_bgc3d_rep_weekly_202112",
        bbox=None,
        maximum_depth=None,
        minimum_depth=None,
        end_datetime="2021-12-29T00:00:00Z",
        start_datetime="1998-01-07T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            variables=variables,
            layer=layer,
            bbox=bbox,
            maximum_depth=maximum_depth,
            minimum_depth=minimum_depth,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
