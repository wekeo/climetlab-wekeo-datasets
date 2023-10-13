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
    "SST_BS_SST_L3S_NRT_OBSERVATIONS_010_013_a",  # noqa: E501 Black sea sst, l3s, 1/16deg daily (sst bs sst l3s NRT observations 010 013 a)
    "SST_BS_SST_L3S_NRT_OBSERVATIONS_010_013_b",  # noqa: E501 Black sea sst, l3s, 1km daily (sst bs sst l3s NRT observations 010 013 b)
]


class sst_bs_sst_l3s_nrt_observations(Main):
    name = "EO:MO:DAT:SST_BS_SST_L3S_NRT_OBSERVATIONS_010_013"
    dataset = "EO:MO:DAT:SST_BS_SST_L3S_NRT_OBSERVATIONS_010_013"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "adjusted_sea_surface_temperature",
            "adjusted_standard_deviation_error",
            "bias_to_reference_sst",
            "l2p_flags",
            "lat",
            "lon",
            "or_latitude",
            "or_longitude",
            "or_number_of_pixels",
            "quality_level",
            "sea_surface_temperature",
            "source_of_sst",
            "sses_bias",
            "sses_standard_deviation",
            "sst_dtime",
            "standard_deviation_to_reference_sst",
            "sum_square_sst",
            "sum_sst",
            "time",
            "wind_speed",
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
        if layer == "SST_BS_SST_L3S_NRT_OBSERVATIONS_010_013_b":
            if start is None:
                start = "2007-12-31T19:00:00Z"

            if end is None:
                end = "2023-09-25T07:00:00Z"

        if layer == "SST_BS_SST_L3S_NRT_OBSERVATIONS_010_013_a":
            if start is None:
                start = "2007-12-31T19:00:00Z"

            if end is None:
                end = "2023-09-25T07:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
