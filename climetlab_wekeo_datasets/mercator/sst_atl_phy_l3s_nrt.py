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
    "cmems_obs-sst_atl_phy_nrt_l3s_P1D-m_202211",  # noqa: E501 Odyssea north-east atlantic sea surface temperature gridded level 3s daily multi-sensor observations
]


class sst_atl_phy_l3s_nrt(Main):
    name = "EO:MO:DAT:SST_ATL_PHY_L3S_NRT_010_037"
    dataset = "EO:MO:DAT:SST_ATL_PHY_L3S_NRT_010_037"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "adjusted_sea_surface_temperature",
            "lat",
            "lon",
            "or_latitude",
            "or_longitude",
            "or_number_of_pixels",
            "quality_level",
            "satellite_zenith_angle",
            "sea_surface_temperature",
            "solar_zenith_angle",
            "source_of_sst",
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
        layer="cmems_obs-sst_atl_phy_nrt_l3s_P1D-m_202211",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-sst_atl_phy_nrt_l3s_P1D-m_202211":
            if start is None:
                start = "2020-12-31T12:00:00Z"

            if end is None:
                end = "2023-10-23T12:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
