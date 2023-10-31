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
    "cmems_obs-oc_atl_bgc-plankton_my_l4-gapfree-multi-1km_P1D_202207",  # noqa: E501 Cmems obs-oc atl bgc-plankton my l4-gapfree-multi-1km p1d
]


class oceancolour_atl_bgc_l4_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_ATL_BGC_L4_MY_009_118"
    dataset = "EO:MO:DAT:OCEANCOLOUR_ATL_BGC_L4_MY_009_118"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "CHL",
            "CHL_uncertainty",
            "flags",
            "lat",
            "lon",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-oc_atl_bgc-plankton_my_l4-gapfree-multi-1km_P1D_202207",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-oc_atl_bgc-plankton_my_l4-gapfree-multi-1km_P1D_202207":
            if start is None:
                start = "1997-09-06T16:08:10Z"

            if end is None:
                end = "2023-10-20T16:59:58Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
