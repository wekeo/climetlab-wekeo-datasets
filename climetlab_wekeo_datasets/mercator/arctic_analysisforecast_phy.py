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
    "cmems_mod_arc_phy_anfc_6km_detided_P1D-m_202311",  # noqa: E501 cmems_mod_arc_phy_anfc_6km_detided_P1D-m
    "cmems_mod_arc_phy_anfc_6km_detided_P1M-m_202311",  # noqa: E501 cmems_mod_arc_phy_anfc_6km_detided_P1M-m
]


class arctic_analysisforecast_phy(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_002_001"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_002_001"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "bottomT",
            "mlotst",
            "model_depth",
            "siage",
            "sialb",
            "siconc",
            "siconc_fy",
            "sisnthick",
            "sithick",
            "so",
            "stfbaro",
            "thetao",
            "vxo",
            "vxsi",
            "vyo",
            "vysi",
            "wo",
            "zos",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-2",
            "-4",
            "-6",
            "-10",
            "-15",
            "-20",
            "-25",
            "-30",
            "-40",
            "-50",
            "-60",
            "-70",
            "-80",
            "-90",
            "-100",
            "-125",
            "-150",
            "-175",
            "-200",
            "-250",
            "-300",
            "-350",
            "-400",
            "-450",
            "-500",
            "-600",
            "-700",
            "-800",
            "-900",
            "-1000",
            "-1200",
            "-1400",
            "-1600",
            "-1800",
            "-2000",
            "-2500",
            "-3000",
            "-3500",
            "-4000",
            "0",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-2",
            "-4",
            "-6",
            "-10",
            "-15",
            "-20",
            "-25",
            "-30",
            "-40",
            "-50",
            "-60",
            "-70",
            "-80",
            "-90",
            "-100",
            "-125",
            "-150",
            "-175",
            "-200",
            "-250",
            "-300",
            "-350",
            "-400",
            "-450",
            "-500",
            "-600",
            "-700",
            "-800",
            "-900",
            "-1000",
            "-1200",
            "-1400",
            "-1600",
            "-1800",
            "-2000",
            "-2500",
            "-3000",
            "-3500",
            "-4000",
            "0",
        ],
    )
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        maximum_depth=None,
        minimum_depth=None,
        end_datetime="2024-06-27T00:00:00Z",
        start_datetime="2021-07-05T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            maximum_depth=maximum_depth,
            minimum_depth=minimum_depth,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
