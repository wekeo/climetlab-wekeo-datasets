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
    "cmems_mod_arc_phy_anfc_nextsim_hm_202211",  # noqa: E501 Nextsim-f sea ice forecast, 3 km hourly-averaged fields (cmems mod arc phy anfc nextsim hm)
    "cmems_mod_arc_phy_anfc_nextsim_P1M-m_202211",  # noqa: E501 Nextsim-f sea ice forecast, 3 km monthly averaged fields (cmems mod arc phy anfc nextsim p1m-m)
]


class arctic_analysisforecast_phy_ice(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_ICE_002_011"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_ICE_002_011"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "latitude",
            "longitude",
            "sialb",
            "siconc",
            "siconc_my",
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
        if layer == "cmems_mod_arc_phy_anfc_nextsim_P1M-m_202211":
            if start is None:
                start = "2019-08-01T00:00:00Z"

            if end is None:
                end = "2023-09-28T00:00:00Z"

        if layer == "cmems_mod_arc_phy_anfc_nextsim_hm_202211":
            if start is None:
                start = "2019-08-02T00:00:00Z"

            if end is None:
                end = "2023-10-25T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
