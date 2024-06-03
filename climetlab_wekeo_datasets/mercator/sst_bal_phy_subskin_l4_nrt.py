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
    "cmems_obs-sst_bal_phy-subskin_nrt_l4_PT1H-m_202211",  # noqa: E501 cmems_obs-sst_bal_phy-subskin_nrt_l4_PT1H-m
]


class sst_bal_phy_subskin_l4_nrt(Main):
    name = "EO:MO:DAT:SST_BAL_PHY_SUBSKIN_L4_NRT_010_034"
    dataset = "EO:MO:DAT:SST_BAL_PHY_SUBSKIN_L4_NRT_010_034"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        bbox,
        layer="cmems_obs-sst_bal_phy-subskin_nrt_l4_PT1H-m_202211",
        max_date="2024-05-05T23:00:00Z",
        min_date="2022-05-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-sst_bal_phy-subskin_nrt_l4_PT1H-m_202211":
            if min_date is None:
                min_date = "2022-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T23:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
