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
    "cmems_obs-oc_blk_bgc-plankton_my_l4-gapfree-multi-1km_P1D_202207",  # noqa: E501 Cmems obs-oc blk bgc-plankton my l4-gapfree-multi-1km p1d
    "cmems_obs-oc_blk_bgc-plankton_my_l4-multi-1km_P1M_202207",  # noqa: E501 Cmems obs-oc blk bgc-plankton my l4-multi-1km p1m
    "cmems_obs-oc_blk_bgc-plankton_my_l4-olci-300m_P1M_202211",  # noqa: E501 Cmems obs-oc blk bgc-plankton my l4-olci-300m p1m
]


class oceancolour_blk_bgc_l4_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_BLK_BGC_L4_MY_009_154"
    dataset = "EO:MO:DAT:OCEANCOLOUR_BLK_BGC_L4_MY_009_154"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "CHL",
            "CHL_count",
            "CHL_error",
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
        layer,
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-oc_blk_bgc-plankton_my_l4-gapfree-multi-1km_P1D_202207":
            if start is None:
                start = "1997-09-16T00:00:00Z"

            if end is None:
                end = "2023-10-16T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-plankton_my_l4-multi-1km_P1M_202207":
            if start is None:
                start = "1997-09-01T00:00:00Z"

            if end is None:
                end = "2023-07-31T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-plankton_my_l4-olci-300m_P1M_202211":
            if start is None:
                start = "2016-04-01T00:00:00Z"

            if end is None:
                end = "2023-07-31T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
