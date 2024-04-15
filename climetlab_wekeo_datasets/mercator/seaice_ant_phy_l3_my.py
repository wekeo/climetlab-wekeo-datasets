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
    "cmems_obs-si_ant_physic_my_drift-amsr_P2D_202311",  # noqa: E501 cmems_obs-si_ant_physic_my_drift-amsr_P2D
    "cmems_obs-si_ant_physic_my_drift-amsr_P3D_202311",  # noqa: E501 cmems_obs-si_ant_physic_my_drift-amsr_P3D
]


class seaice_ant_phy_l3_my(Main):
    name = "EO:MO:DAT:SEAICE_ANT_PHY_L3_MY_011_018"
    dataset = "EO:MO:DAT:SEAICE_ANT_PHY_L3_MY_011_018"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        layer,
        bbox,
        max_date="2023-11-03T00:00:00Z",
        min_date="2003-04-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-si_ant_physic_my_drift-amsr_P2D_202311":
            if min_date is None:
                min_date = "2003-04-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-02T00:00:00Z"

        if layer == "cmems_obs-si_ant_physic_my_drift-amsr_P3D_202311":
            if min_date is None:
                min_date = "2003-04-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-03T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
