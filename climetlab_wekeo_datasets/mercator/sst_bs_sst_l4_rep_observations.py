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
    "cmems_SST_BS_SST_L4_REP_OBSERVATIONS_010_022_202007",  # noqa: E501 Black sea sst analysis l4, reprocessed using esa cci sst v.2.0, c3s v.2.0 and pfv53 data, 0.05 deg. daily (cmems sst bs sst l4 rep observations 010 022)
]


class sst_bs_sst_l4_rep_observations(Main):
    name = "EO:MO:DAT:SST_BS_SST_L4_REP_OBSERVATIONS_010_022"
    dataset = "EO:MO:DAT:SST_BS_SST_L4_REP_OBSERVATIONS_010_022"

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
        layer="cmems_SST_BS_SST_L4_REP_OBSERVATIONS_010_022_202007",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_SST_BS_SST_L4_REP_OBSERVATIONS_010_022_202007":
            if start is None:
                start = "1981-08-24T19:00:00Z"

            if end is None:
                end = "2023-03-29T07:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
