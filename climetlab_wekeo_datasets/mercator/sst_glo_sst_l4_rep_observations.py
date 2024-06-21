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

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "analysed_sst",
            "analysed_sst_uncertainty",
            "mask",
            "sea_ice_fraction",
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
        end_datetime="2022-10-31T00:00:00Z",
        start_datetime="2017-01-01T00:00:00Z",
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
