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
    "cmems-IFREMER-ATL-SST-L4-REP-OBS_FULL_TIME_SERIE_202012",  # noqa: E501 cmems-IFREMER-ATL-SST-L4-REP-OBS_FULL_TIME_SERIE
]


class sst_atl_sst_l4_rep_observations(Main):
    name = "EO:MO:DAT:SST_ATL_SST_L4_REP_OBSERVATIONS_010_026"
    dataset = "EO:MO:DAT:SST_ATL_SST_L4_REP_OBSERVATIONS_010_026"

    @normalize(
        "variables",
        [
            "analysed_sst",
            "analysis_error",
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
        layer="cmems-IFREMER-ATL-SST-L4-REP-OBS_FULL_TIME_SERIE_202012",
        bbox=None,
        end_datetime="2020-12-31T00:00:00Z",
        start_datetime="1982-01-01T00:00:00Z",
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
