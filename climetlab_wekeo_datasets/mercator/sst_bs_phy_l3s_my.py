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
    "cmems_obs-sst_bs_phy_my_l3s_P1D-m_202211",  # noqa: E501 cmems_obs-sst_bs_phy_my_l3s_P1D-m
]


class sst_bs_phy_l3s_my(Main):
    name = "EO:MO:DAT:SST_BS_PHY_L3S_MY_010_041"
    dataset = "EO:MO:DAT:SST_BS_PHY_L3S_MY_010_041"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "adjusted_sea_surface_temperature",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(
        self,
        layer="cmems_obs-sst_bs_phy_my_l3s_P1D-m_202211",
        variables="adjusted_sea_surface_temperature",
        bbox=None,
        limit=None,
    ):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
