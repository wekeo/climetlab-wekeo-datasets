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
    "cnes_obs-sl_glo_phy-mdt_my_0.125deg_P20Y_202012",  # noqa: E501 Mdt hybrid cnes-cls18 cmems2020 global
]


class sealevel_glo_phy_mdt(Main):
    name = "EO:MO:DAT:SEALEVEL_GLO_PHY_MDT_008_063"
    dataset = "EO:MO:DAT:SEALEVEL_GLO_PHY_MDT_008_063"

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
        layer="cnes_obs-sl_glo_phy-mdt_my_0.125deg_P20Y_202012",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cnes_obs-sl_glo_phy-mdt_my_0.125deg_P20Y_202012":
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
