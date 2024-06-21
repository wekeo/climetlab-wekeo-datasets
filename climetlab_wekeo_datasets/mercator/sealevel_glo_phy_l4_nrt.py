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
    "cmems_obs-sl_glo_phy-ssh_nrt_allsat-l4-duacs-0.25deg_P1D_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_allsat-l4-duacs-0.25deg_P1D
]


class sealevel_glo_phy_l4_nrt(Main):
    name = "EO:MO:DAT:SEALEVEL_GLO_PHY_L4_NRT_008_046"
    dataset = "EO:MO:DAT:SEALEVEL_GLO_PHY_L4_NRT_008_046"

    @normalize(
        "variables",
        [
            "adt",
            "err_sla",
            "err_ugosa",
            "err_vgosa",
            "flag_ice",
            "sla",
            "ugos",
            "ugosa",
            "vgos",
            "vgosa",
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
        layer="cmems_obs-sl_glo_phy-ssh_nrt_allsat-l4-duacs-0.25deg_P1D_202311",
        bbox=None,
        end_datetime="2024-06-20T00:00:00Z",
        start_datetime="2022-01-01T00:00:00Z",
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
