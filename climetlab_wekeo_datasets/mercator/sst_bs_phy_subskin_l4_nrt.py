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
    "cmems_obs-sst_blk_phy-sst_nrt_diurnal-oi-0.0625deg_PT1H-m_202105",  # noqa: E501 Black sea diurnal subskin sst analysis, l4, 1/16deg hourly
]


class sst_bs_phy_subskin_l4_nrt(Main):
    name = "EO:MO:DAT:SST_BS_PHY_SUBSKIN_L4_NRT_010_035"
    dataset = "EO:MO:DAT:SST_BS_PHY_SUBSKIN_L4_NRT_010_035"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "analysed_sst",
            "analysis_error",
            "lat",
            "lon",
            "mask",
            "sea_ice_fraction",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-sst_blk_phy-sst_nrt_diurnal-oi-0.0625deg_PT1H-m_202105",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-sst_blk_phy-sst_nrt_diurnal-oi-0.0625deg_PT1H-m_202105":
            if start is None:
                start = "2019-12-31T23:30:00Z"

            if end is None:
                end = "2023-09-24T23:30:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
