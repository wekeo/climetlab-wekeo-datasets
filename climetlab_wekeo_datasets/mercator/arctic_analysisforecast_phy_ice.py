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
    "cmems_mod_arc_phy_anfc_nextsim_hm_202211",  # noqa: E501 cmems_mod_arc_phy_anfc_nextsim_hm_202211
    "cmems_mod_arc_phy_anfc_nextsim_hm_202311",  # noqa: E501 cmems_mod_arc_phy_anfc_nextsim_hm_202311
    "cmems_mod_arc_phy_anfc_nextsim_P1M-m_202211",  # noqa: E501 cmems_mod_arc_phy_anfc_nextsim_P1M-m_202211
    "cmems_mod_arc_phy_anfc_nextsim_P1M-m_202311",  # noqa: E501 cmems_mod_arc_phy_anfc_nextsim_P1M-m
]


class arctic_analysisforecast_phy_ice(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_ICE_002_011"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_ICE_002_011"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "latitude",
            "longitude",
            "si_ridge_ratio",
            "siage",
            "sialb",
            "siconc",
            "siconc_my",
            "siconc_young",
            "sisnthick",
            "sithick",
            "stereographic",
            "time",
            "time_bnds",
            "vxsi",
            "vysi",
            "x",
            "y",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-04-10T23:30:00Z",
        min_date="2019-08-01T00:29:59Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_arc_phy_anfc_nextsim_P1M-m_202211":
            if min_date is None:
                min_date = "2019-08-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-16T12:00:00Z"

        if layer == "cmems_mod_arc_phy_anfc_nextsim_P1M-m_202311":
            if min_date is None:
                min_date = "2019-08-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T12:00:00Z"

        if layer == "cmems_mod_arc_phy_anfc_nextsim_hm_202211":
            if min_date is None:
                min_date = "2019-08-01T00:29:59Z"

            if max_date is None:
                max_date = "2024-04-10T23:30:00Z"

        if layer == "cmems_mod_arc_phy_anfc_nextsim_hm_202311":
            if min_date is None:
                min_date = "2019-08-01T00:29:59Z"

            if max_date is None:
                max_date = "2024-05-27T23:30:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
