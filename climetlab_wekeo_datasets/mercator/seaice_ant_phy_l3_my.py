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
    "cmems_obs-si_ant_physic_my_drift-amsr_P2D_202112",  # noqa: E501 Antarctic ocean - sea ice - 2 days drift, amsr
    "cmems_obs-si_ant_physic_my_drift-amsr_P3D_202112",  # noqa: E501 Antarctic ocean - sea ice - 3 days drift, amsr
]


class seaice_ant_phy_l3_my(Main):
    name = "EO:MO:DAT:SEAICE_ANT_PHY_L3_MY_011_018"
    dataset = "EO:MO:DAT:SEAICE_ANT_PHY_L3_MY_011_018"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "depth",
            "eastward_sea_ice_velocity",
            "latitude",
            "longitude",
            "northward_sea_ice_velocity",
            "time",
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
        if layer == "cmems_obs-si_ant_physic_my_drift-amsr_P2D_202112":
            if start is None:
                start = "2003-04-01T00:00:00Z"

            if end is None:
                end = "2023-04-03T00:00:00Z"

        if layer == "cmems_obs-si_ant_physic_my_drift-amsr_P3D_202112":
            if start is None:
                start = "2003-04-01T00:00:00Z"

            if end is None:
                end = "2023-04-04T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
