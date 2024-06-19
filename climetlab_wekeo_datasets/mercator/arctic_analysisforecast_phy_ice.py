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
    "cmems_mod_arc_phy_anfc_nextsim_P1M-m_202311",  # noqa: E501 cmems_mod_arc_phy_anfc_nextsim_P1M-m
]


class arctic_analysisforecast_phy_ice(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_ICE_002_011"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_ICE_002_011"

    @normalize(
        "variables",
        [
            "si_ridge_ratio",
            "siage",
            "sialb",
            "siconc",
            "siconc_my",
            "siconc_young",
            "sisnthick",
            "sithick",
            "vxsi",
            "vysi",
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
        layer="cmems_mod_arc_phy_anfc_nextsim_P1M-m_202311",
        bbox=None,
        end_datetime="2024-05-01T00:00:00Z",
        start_datetime="2019-08-01T00:00:00Z",
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
