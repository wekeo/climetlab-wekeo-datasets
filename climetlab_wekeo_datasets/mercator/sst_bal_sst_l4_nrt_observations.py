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
    "DMI-BALTIC-SST-L4-NRT-OBS_FULL_TIME_SERIE",  # noqa: E501 Baltic sea - sst analysis
]


class sst_bal_sst_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SST_BAL_SST_L4_NRT_OBSERVATIONS_010_007_b"
    dataset = "EO:MO:DAT:SST_BAL_SST_L4_NRT_OBSERVATIONS_010_007_b"

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
        layer="DMI-BALTIC-SST-L4-NRT-OBS_FULL_TIME_SERIE",
        max_date="2024-04-02T00:00:00Z",
        min_date="2016-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "DMI-BALTIC-SST-L4-NRT-OBS_FULL_TIME_SERIE":
            if min_date is None:
                min_date = "2016-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
