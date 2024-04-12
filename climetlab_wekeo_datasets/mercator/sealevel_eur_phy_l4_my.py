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
    "cmems_obs-sl_eur_phy-ssh_my_allsat-l4-duacs-0.125deg_P1D_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_allsat-l4-duacs-0.125deg_P1D
    "cmems_obs-sl_eur_phy-ssh_my_allsat-l4-duacs-0.125deg_P1D_202112",  # noqa: E501 Dt merged all satellites european seas gridded ssalto/duacs sea surface height l4 product and derived variables
    "cmems_obs-sl_eur_phy-ssh_myint_allsat-l4-duacs-0.125deg_P1D_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_myint_allsat-l4-duacs-0.125deg_P1D_202311
]


class sealevel_eur_phy_l4_my(Main):
    name = "EO:MO:DAT:SEALEVEL_EUR_PHY_L4_MY_008_068"
    dataset = "EO:MO:DAT:SEALEVEL_EUR_PHY_L4_MY_008_068"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
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
            "tpa_correction",
            "ugos",
            "ugosa",
            "vgos",
            "vgosa",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2022-08-03T12:00:00Z",
        min_date="2022-07-31T12:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-sl_eur_phy-ssh_my_allsat-l4-duacs-0.125deg_P1D_202112":
            if min_date is None:
                min_date = "1992-12-31T12:00:00Z"

            if max_date is None:
                max_date = "2023-06-07T12:00:00Z"

        if (
            layer
            == "cmems_obs-sl_eur_phy-ssh_myint_allsat-l4-duacs-0.125deg_P1D_202311"
        ):
            if min_date is None:
                min_date = "2022-07-31T12:00:00Z"

            if max_date is None:
                max_date = "2022-08-03T12:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
