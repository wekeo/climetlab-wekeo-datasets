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
    @normalize("bbox", "bounding-box(list)")
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
            "sst_anomaly",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-04-02T00:00:00Z",
        min_date="2007-12-31T19:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_b":
            if min_date is None:
                min_date = "2007-12-31T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T00:00:00Z"

        if layer == "SST_BS_SSTA_L4_NRT_OBSERVATIONS_010_006_d":
            if min_date is None:
                min_date = "2007-12-31T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T00:00:00Z"

        if layer == "SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_a_V2_202311":
            if min_date is None:
                min_date = "2007-12-31T19:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T00:00:00Z"

        if layer == "SST_BS_SST_L4_NRT_OBSERVATIONS_010_006_c_V2_202311":
            if min_date is None:
                min_date = "2007-12-31T19:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
