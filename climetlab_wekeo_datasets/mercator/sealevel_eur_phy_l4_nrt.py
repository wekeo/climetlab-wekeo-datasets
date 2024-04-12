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
    "cmems_obs-sl_eur_phy-ssh_nrt_allsat-l4-duacs-0.125deg_P1D_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_allsat-l4-duacs-0.125deg_P1D
]


class sealevel_eur_phy_l4_nrt(Main):
    name = "EO:MO:DAT:SEALEVEL_EUR_PHY_L4_NRT_008_060"
    dataset = "EO:MO:DAT:SEALEVEL_EUR_PHY_L4_NRT_008_060"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
            "ugos",
            "ugosa",
            "vgos",
            "vgosa",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="cmems_obs-sl_eur_phy-ssh_nrt_allsat-l4-duacs-0.125deg_P1D_202311",
        max_date="2024-04-02T00:00:00Z",
        min_date="2021-12-31T12:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_allsat-l4-duacs-0.125deg_P1D_202311":
            if min_date is None:
                min_date = "2021-12-31T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
