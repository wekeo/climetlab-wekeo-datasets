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
    "cmems_obs-sl_med_phy-mdt_my_l4-0.0417deg_P20Y_202105",  # noqa: E501 Mdt cmems 2020 med
]


class sealevel_med_phy_mdt_l4_static(Main):
    name = "EO:MO:DAT:SEALEVEL_MED_PHY_MDT_L4_STATIC_008_066"
    dataset = "EO:MO:DAT:SEALEVEL_MED_PHY_MDT_L4_STATIC_008_066"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "climatology_bnds",
            "crs",
            "err_mdt",
            "err_u",
            "err_v",
            "lat_bnds",
            "latitude",
            "lon_bnds",
            "longitude",
            "mdt",
            "nv",
            "time",
            "u",
            "v",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-sl_med_phy-mdt_my_l4-0.0417deg_P20Y_202105",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-sl_med_phy-mdt_my_l4-0.0417deg_P20Y_202105":
            if start is None:
                start = "1993-01-01T00:00:00Z"

            if end is None:
                end = "2013-01-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
