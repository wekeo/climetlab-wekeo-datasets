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
    "cmems_obs-wave_glo_phy-spc_nrt_multi-l4-1deg_PT3H_202112",  # noqa: E501 NRT merged all sentinel-1 global ocean gridded spectral parameters l4 product and derived variables
]


class wave_glo_phy_spc_l4_nrt(Main):
    name = "EO:MO:DAT:WAVE_GLO_PHY_SPC_L4_NRT_014_004"
    dataset = "EO:MO:DAT:WAVE_GLO_PHY_SPC_L4_NRT_014_004"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "VAVH_NBR_SW0",
            "VAVH_NBR_SW1",
            "VAVH_NBR_SW2",
            "VAVH_NBR_SW3",
            "VAVH_NBR_SW4",
            "VAVH_SW0",
            "VAVH_SW1",
            "VAVH_SW2",
            "VAVH_SW3",
            "VAVH_SW4",
            "VPED_NBR_SW0",
            "VPED_NBR_SW1",
            "VPED_NBR_SW2",
            "VPED_NBR_SW3",
            "VPED_NBR_SW4",
            "VPED_SW0",
            "VPED_SW1",
            "VPED_SW2",
            "VPED_SW3",
            "VPED_SW4",
            "VTPK_NBR_SW0",
            "VTPK_NBR_SW1",
            "VTPK_NBR_SW2",
            "VTPK_NBR_SW3",
            "VTPK_NBR_SW4",
            "VTPK_SW0",
            "VTPK_SW1",
            "VTPK_SW2",
            "VTPK_SW3",
            "VTPK_SW4",
            "latitude",
            "longitude",
            "storm_name",
            "storm_number_SW0",
            "storm_number_SW1",
            "storm_number_SW2",
            "storm_number_SW3",
            "storm_number_SW4",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-wave_glo_phy-spc_nrt_multi-l4-1deg_PT3H_202112",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-wave_glo_phy-spc_nrt_multi-l4-1deg_PT3H_202112":
            if start is None:
                start = "2021-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-30T23:59:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
