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
    "cmems_obs_oc_blk_bgc_tur-spm-chl_nrt_l4-hr-mosaic_P1D-m_202107",  # noqa: E501 cmems_obs_oc_blk_bgc_tur-spm-chl_nrt_l4-hr-mosaic_P1D-m
]


class oceancolour_blk_bgc_hr_l4_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_BLK_BGC_HR_L4_NRT_009_212"
    dataset = "EO:MO:DAT:OCEANCOLOUR_BLK_BGC_HR_L4_NRT_009_212"

    @normalize(
        "variables",
        [
            "CHL",
            "SPM",
            "TUR",
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
        layer="cmems_obs_oc_blk_bgc_tur-spm-chl_nrt_l4-hr-mosaic_P1D-m_202107",
        bbox=None,
        end_datetime="2023-10-31T00:00:00Z",
        start_datetime="2020-01-02T00:00:00Z",
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
