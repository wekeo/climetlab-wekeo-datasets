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

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "CHL",
            "CHL_count",
            "CHL_error",
            "KD490",
            "KD490_count",
            "KD490_error",
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
        end_datetime="2024-05-01T00:00:00Z",
        start_datetime="2022-01-01T00:00:00Z",
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
