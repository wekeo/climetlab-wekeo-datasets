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
    "SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_a_V2",  # noqa: E501 Black sea sst analysis, l4, 1/16deg daily (sst bs sst l4 NRT observations 010 006 a v2)
    "SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_c_V2",  # noqa: E501 Black sea sst analysis, l4, 1km daily (sst bs sst l4 NRT observations 010 006 c v2)
    "SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_b",  # noqa: E501 Black sea sst anomaly, l4, 1/16deg daily (sst bs ssta l4 NRT observations 010 006 b)
    "SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_d",  # noqa: E501 Black sea sst anomaly, l4, 1km daily (sst bs ssta l4 NRT observations 010 006 d)
]


class sst_bs_sst_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SST_BS_SST_L4_NRT_OBSERVATIONS_010_006"
    dataset = "EO:MO:DAT:SST_BS_SST_L4_NRT_OBSERVATIONS_010_006"

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
            "sst_anomaly",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer,
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_b":
            if start is None:
                start = "2007-12-31T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_d":
            if start is None:
                start = "2007-12-31T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_a_V2":
            if start is None:
                start = "2007-12-31T19:00:00Z"

            if end is None:
                end = "2023-10-28T07:00:00Z"

        if layer == "SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_c_V2":
            if start is None:
                start = "2007-12-31T19:00:00Z"

            if end is None:
                end = "2023-10-28T07:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
