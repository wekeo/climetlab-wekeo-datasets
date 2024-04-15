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
    "cmems_mod_arc_phy_my_topaz4_P1D-m_202211",  # noqa: E501 cmems_mod_arc_phy_my_topaz4_P1D-m
    "cmems_mod_arc_phy_my_topaz4_P1M_202012",  # noqa: E501 cmems_mod_arc_phy_my_topaz4_P1M
    "cmems_mod_arc_phy_my_topaz4_P1Y_202211",  # noqa: E501 cmems_mod_arc_phy_my_topaz4_P1Y
]


class arctic_multiyear_phy(Main):
    name = "EO:MO:DAT:ARCTIC_MULTIYEAR_PHY_002_003"
    dataset = "EO:MO:DAT:ARCTIC_MULTIYEAR_PHY_002_003"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "latitude",
            "longitude",
            "mlotst",
            "model_depth",
            "siconc",
            "sisnthick",
            "sithick",
            "so",
            "stereographic",
            "stfbaro",
            "thetao",
            "time",
            "vxo",
            "vxsi",
            "vyo",
            "vysi",
            "x",
            "y",
            "zos",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2022-01-01T00:00:00Z",
        min_date="1991-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_arc_phy_my_topaz4_P1D-m_202211":
            if min_date is None:
                min_date = "1991-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-12-31T00:00:00Z"

        if layer == "cmems_mod_arc_phy_my_topaz4_P1M_202012":
            if min_date is None:
                min_date = "1991-01-15T00:00:00Z"

            if max_date is None:
                max_date = "2022-12-15T00:00:00Z"

        if layer == "cmems_mod_arc_phy_my_topaz4_P1Y_202211":
            if min_date is None:
                min_date = "1991-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-01-01T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
