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
    "C3S-GLO-SST-L4-REP-OBS-SST_202211",  # noqa: E501 C3S-GLO-SST-L4-REP-OBS-SST
    "ESACCI-GLO-SST-L4-REP-OBS-SST_202211",  # noqa: E501 ESACCI-GLO-SST-L4-REP-OBS-SST
]


class sst_glo_sst_l4_rep_observations(Main):
    name = "EO:MO:DAT:SST_GLO_SST_L4_REP_OBSERVATIONS_010_024"
    dataset = "EO:MO:DAT:SST_GLO_SST_L4_REP_OBSERVATIONS_010_024"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "analysed_sst",
            "analysed_sst_uncertainty",
            "lat",
            "lat_bnds",
            "lon",
            "lon_bnds",
            "mask",
            "sea_ice_fraction",
            "time",
            "time_bnds",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2017-01-01T00:00:00Z",
        min_date="1981-09-01T00:00:00Z",

        variables=None,
        limit=None,
    ):
        if layer == "C3S-GLO-SST-L4-REP-OBS-SST_202211":
            if min_date is None:
                min_date = "2017-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "ESACCI-GLO-SST-L4-REP-OBS-SST_202211":
            if min_date is None:
                min_date = "1981-09-01T00:00:00Z"

            if max_date is None:
                max_date = "2017-01-01T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            
            variables=variables,
            limit=limit,
        )
