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
    "SST_MED_SST_L3S_NRT_OBSERVATIONS_010_012_a_202311",  # noqa: E501 SST_MED_SST_L3S_NRT_OBSERVATIONS_010_012_a
    "SST_MED_SST_L3S_NRT_OBSERVATIONS_010_012_b_202311",  # noqa: E501 SST_MED_SST_L3S_NRT_OBSERVATIONS_010_012_b
]


class sst_med_sst_l3s_nrt_observations(Main):
    name = "EO:MO:DAT:SST_MED_SST_L3S_NRT_OBSERVATIONS_010_012"
    dataset = "EO:MO:DAT:SST_MED_SST_L3S_NRT_OBSERVATIONS_010_012"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "adjusted_sea_surface_temperature",
            "adjusted_standard_deviation_error",
            "bias_to_reference_sst",
            "l2p_flags",
            "or_latitude",
            "or_longitude",
            "or_number_of_pixels",
            "quality_level",
            "sea_surface_temperature",
            "sources_of_sst",
            "sses_bias",
            "sses_standard_deviation",
            "sst_dtime",
            "standard_deviation_to_reference_sst",
            "sum_square_sst",
            "sum_sst",
            "wind_speed",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        end_datetime="2024-06-20T00:00:00Z",
        start_datetime="2008-01-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
