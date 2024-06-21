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
    "cmems_obs-sst_med_phy-sst_nrt_diurnal-oi-0.0625deg_PT1H-m_202105",  # noqa: E501 cmems_obs-sst_med_phy-sst_nrt_diurnal-oi-0.0625deg_PT1H-m
]


class sst_med_phy_subskin_l4_nrt(Main):
    name = "EO:MO:DAT:SST_MED_PHY_SUBSKIN_L4_NRT_010_036"
    dataset = "EO:MO:DAT:SST_MED_PHY_SUBSKIN_L4_NRT_010_036"

    @normalize(
        "variables",
        [
            "analysed_sst",
            "analysis_error",
            "mask",
            "sea_ice_fraction",
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
        layer="cmems_obs-sst_med_phy-sst_nrt_diurnal-oi-0.0625deg_PT1H-m_202105",
        bbox=None,
        end_datetime="2024-06-19T23:00:00Z",
        start_datetime="2019-01-01T00:00:00Z",
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
