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
    "cmems_obs-sl_eur_phy-ssh_my_allsat-l4-duacs-0.125deg_P1D_202112",  # noqa: E501 Dt merged all satellites european seas gridded ssalto/duacs sea surface height l4 product and derived variables
]


class sealevel_eur_phy_l4_my(Main):
    name = "EO:MO:DAT:SEALEVEL_EUR_PHY_L4_MY_008_068"
    dataset = "EO:MO:DAT:SEALEVEL_EUR_PHY_L4_MY_008_068"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "adt",
            "crs",
            "err_sla",
            "err_ugosa",
            "err_vgosa",
            "flag_ice",
            "lat_bnds",
            "latitude",
            "lon_bnds",
            "longitude",
            "nv",
            "sla",
            "time",
            "tpa_correction",
            "ugos",
            "ugosa",
            "vgos",
            "vgosa",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-sl_eur_phy-ssh_my_allsat-l4-duacs-0.125deg_P1D_202112",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-sl_eur_phy-ssh_my_allsat-l4-duacs-0.125deg_P1D_202112":
            if start is None:
                start = "1992-12-31T12:00:00Z"

            if end is None:
                end = "2022-08-04T12:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
