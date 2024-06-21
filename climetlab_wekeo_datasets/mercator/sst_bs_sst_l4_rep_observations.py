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
    "cmems_SST_BS_SST_L4_REP_OBSERVATIONS_010_022_202007",  # noqa: E501 cmems_SST_BS_SST_L4_REP_OBSERVATIONS_010_022
]


class sst_bs_sst_l4_rep_observations(Main):
    name = "EO:MO:DAT:SST_BS_SST_L4_REP_OBSERVATIONS_010_022"
    dataset = "EO:MO:DAT:SST_BS_SST_L4_REP_OBSERVATIONS_010_022"

    @normalize(
        "variables",
        [
            "analysed_sst",
            "analysis_error",
            "mask",
            "sea_ice_fraction",
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        variables,
        layer="cmems_SST_BS_SST_L4_REP_OBSERVATIONS_010_022_202007",
        bbox=None,
        end_datetime="2024-05-20T00:00:00Z",
        start_datetime="1981-08-25T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            variables=variables,
            layer=layer,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
