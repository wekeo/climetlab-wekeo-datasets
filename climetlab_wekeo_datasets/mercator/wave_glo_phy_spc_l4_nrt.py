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
    "cmems_obs-wave_glo_phy-spc_nrt_multi-l4-1deg_PT3H_202112",  # noqa: E501 cmems_obs-wave_glo_phy-spc_nrt_multi-l4-1deg_PT3H
]


class wave_glo_phy_spc_l4_nrt(Main):
    name = "EO:MO:DAT:WAVE_GLO_PHY_SPC_L4_NRT_014_004"
    dataset = "EO:MO:DAT:WAVE_GLO_PHY_SPC_L4_NRT_014_004"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        bbox,
        layer="cmems_obs-wave_glo_phy-spc_nrt_multi-l4-1deg_PT3H_202112",
        max_date="2024-04-30T21:00:00Z",
        min_date="2021-11-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-wave_glo_phy-spc_nrt_multi-l4-1deg_PT3H_202112":
            if min_date is None:
                min_date = "2021-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-30T21:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
