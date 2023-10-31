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
    "cmems_obs-si_arc_phy_my_L3S-DMIOI_P1D-m_202211",  # noqa: E501 Dmi arctic sst/ist, l3s , (seaice arc phy climate l3 my 011 021)
]


class seaice_arc_phy_climate_l3_my(Main):
    name = "EO:MO:DAT:SEAICE_ARC_PHY_CLIMATE_L3_MY_011_021"
    dataset = "EO:MO:DAT:SEAICE_ARC_PHY_CLIMATE_L3_MY_011_021"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "analysed_st",
            "lat",
            "lon",
            "mask",
            "or_number_of_st_pixels",
            "quality_level",
            "sea_ice_fraction",
            "source_of_st",
            "sses_bias",
            "sses_standard_deviation",
            "st_dtime",
            "sum_square_st",
            "sum_st",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-si_arc_phy_my_L3S-DMIOI_P1D-m_202211",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-si_arc_phy_my_L3S-DMIOI_P1D-m_202211":
            if start is None:
                start = "1982-01-01T00:00:00Z"

            if end is None:
                end = "2021-06-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
