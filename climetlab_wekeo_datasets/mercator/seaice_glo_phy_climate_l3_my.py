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
    "c3s_obs-si_glo_phy_my_nh-l3_P1M_202311",  # noqa: E501 c3s_obs-si_glo_phy_my_nh-l3_P1M
]


class seaice_glo_phy_climate_l3_my(Main):
    name = "EO:MO:DAT:SEAICE_GLO_PHY_CLIMATE_L3_MY_011_013"
    dataset = "EO:MO:DAT:SEAICE_GLO_PHY_CLIMATE_L3_MY_011_013"

    @normalize(
        "variables",
        [
            "quality_flag",
            "sea_ice_thickness",
            "status_flag",
            "uncertainty",
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        variables,
        layer="c3s_obs-si_glo_phy_my_nh-l3_P1M_202311",
        bbox=None,
        end_datetime="2020-04-01T00:00:00Z",
        start_datetime="2002-10-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            variables=variables,
            layer=layer,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
