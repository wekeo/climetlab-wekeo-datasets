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
    "cmems_obs_si_arc_phy_my_L4-DMIOI_P1D-m_202105",  # noqa: E501 cmems_obs_si_arc_phy_my_L4-DMIOI_P1D-m
]


class seaice_arc_phy_climate_l4_my(Main):
    name = "EO:MO:DAT:SEAICE_ARC_PHY_CLIMATE_L4_MY_011_016"
    dataset = "EO:MO:DAT:SEAICE_ARC_PHY_CLIMATE_L4_MY_011_016"

    @normalize(
        "variables",
        [
            "analysed_st",
            "analysis_error",
            "mask",
            "observation_max",
            "observation_min",
            "observation_num",
            "observation_std",
            "sea_ice_fraction",
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
        layer="cmems_obs_si_arc_phy_my_L4-DMIOI_P1D-m_202105",
        bbox=None,
        end_datetime="2022-12-31T00:00:00Z",
        start_datetime="1982-01-01T00:00:00Z",
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
