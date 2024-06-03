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
    "cmems_obs-oc_blk_bgc-plankton_nrt_l4-gapfree-multi-1km_P1D_202207",  # noqa: E501 cmems_obs-oc_blk_bgc-plankton_nrt_l4-gapfree-multi-1km_P1D
    "cmems_obs-oc_blk_bgc-plankton_nrt_l4-multi-1km_P1M_202207",  # noqa: E501 cmems_obs-oc_blk_bgc-plankton_nrt_l4-multi-1km_P1M
    "cmems_obs-oc_blk_bgc-plankton_nrt_l4-olci-300m_P1M_202207",  # noqa: E501 cmems_obs-oc_blk_bgc-plankton_nrt_l4-olci-300m_P1M
    "cmems_obs-oc_blk_bgc-transp_nrt_l4-multi-1km_P1M_202207",  # noqa: E501 cmems_obs-oc_blk_bgc-transp_nrt_l4-multi-1km_P1M
    "cmems_obs-oc_blk_bgc-transp_nrt_l4-olci-300m_P1M_202207",  # noqa: E501 cmems_obs-oc_blk_bgc-transp_nrt_l4-olci-300m_P1M
]


class oceancolour_blk_bgc_l4_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_BLK_BGC_L4_NRT_009_152"
    dataset = "EO:MO:DAT:OCEANCOLOUR_BLK_BGC_L4_NRT_009_152"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "CHL",
            "CHL_count",
            "CHL_error",
            "KD490",
            "KD490_count",
            "KD490_error",
            "lat",
            "lon",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-05-05T00:00:00Z",
        min_date="2023-12-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-oc_blk_bgc-plankton_nrt_l4-gapfree-multi-1km_P1D_202207":
            if min_date is None:
                min_date = "2023-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-plankton_nrt_l4-multi-1km_P1M_202207":
            if min_date is None:
                min_date = "2023-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-plankton_nrt_l4-olci-300m_P1M_202207":
            if min_date is None:
                min_date = "2023-10-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-transp_nrt_l4-multi-1km_P1M_202207":
            if min_date is None:
                min_date = "2022-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-transp_nrt_l4-olci-300m_P1M_202207":
            if min_date is None:
                min_date = "2022-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
