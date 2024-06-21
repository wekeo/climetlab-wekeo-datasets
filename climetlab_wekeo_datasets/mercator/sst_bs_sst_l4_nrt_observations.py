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
    "SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_a_V2_202311",  # noqa: E501 SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_a_V2
    "SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_c_V2_202311",  # noqa: E501 SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_c_V2
    "SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_b",  # noqa: E501 SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_b
    "SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_d",  # noqa: E501 SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_d
]


class sst_bs_sst_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SST_BS_SST_L4_NRT_OBSERVATIONS_010_006"
    dataset = "EO:MO:DAT:SST_BS_SST_L4_NRT_OBSERVATIONS_010_006"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "analysed_sst",
            "analysis_error",
            "mask",
            "sea_ice_fraction",
            "sst_anomaly",
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
