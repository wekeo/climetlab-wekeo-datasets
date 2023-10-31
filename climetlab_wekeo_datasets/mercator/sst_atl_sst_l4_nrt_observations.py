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
    "IFREMER-ATL-SST-L4-NRT-OBS_FULL_TIME_SERIE_201904",  # noqa: E501 Atlantic european north west shelf ocean - sst analysis - odyssea
]


class sst_atl_sst_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SST_ATL_SST_L4_NRT_OBSERVATIONS_010_025"
    dataset = "EO:MO:DAT:SST_ATL_SST_L4_NRT_OBSERVATIONS_010_025"

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
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="IFREMER-ATL-SST-L4-NRT-OBS_FULL_TIME_SERIE_201904",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "IFREMER-ATL-SST-L4-NRT-OBS_FULL_TIME_SERIE_201904":
            if start is None:
                start = "2017-12-31T12:00:00Z"

            if end is None:
                end = "2023-10-26T12:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
