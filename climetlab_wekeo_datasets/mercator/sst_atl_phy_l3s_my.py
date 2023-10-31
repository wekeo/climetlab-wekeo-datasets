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
    "cmems_obs-sst_atl_phy_my_l3s_P1D-m_202211",  # noqa: E501 Merged collation of sea surface temperature from multiple satellite sources
]


class sst_atl_phy_l3s_my(Main):
    name = "EO:MO:DAT:SST_ATL_PHY_L3S_MY_010_038"
    dataset = "EO:MO:DAT:SST_ATL_PHY_L3S_MY_010_038"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "adjusted_sea_surface_temperature",
            "bias_to_reference_sst",
            "lat",
            "lon",
            "quality_level",
            "sea_surface_temperature",
            "sources_of_sst",
            "sses_bias",
            "sses_standard_deviation",
            "sst_dtime",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-sst_atl_phy_my_l3s_P1D-m_202211",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-sst_atl_phy_my_l3s_P1D-m_202211":
            if start is None:
                start = "1982-01-01T00:00:00Z"

            if end is None:
                end = "2022-01-02T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
