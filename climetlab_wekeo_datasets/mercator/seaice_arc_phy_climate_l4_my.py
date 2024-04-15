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

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "analysed_st",
            "analysis_error",
            "lat",
            "lon",
            "mask",
            "observation_max",
            "observation_min",
            "observation_num",
            "observation_std",
            "sea_ice_fraction",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="cmems_obs_si_arc_phy_my_L4-DMIOI_P1D-m_202105",
        max_date="2022-07-01T00:00:00Z",
        min_date="1982-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs_si_arc_phy_my_L4-DMIOI_P1D-m_202105":
            if min_date is None:
                min_date = "1982-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-07-01T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
