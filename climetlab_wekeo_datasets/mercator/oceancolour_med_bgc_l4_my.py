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
    "cmems_obs-oc_med_bgc-plankton_my_l4-gapfree-multi-1km_P1D_202311",  # noqa: E501 cmems_obs-oc_med_bgc-plankton_my_l4-gapfree-multi-1km_P1D
    "cmems_obs-oc_med_bgc-plankton_my_l4-multi-1km_P1M_202311",  # noqa: E501 cmems_obs-oc_med_bgc-plankton_my_l4-multi-1km_P1M
    "cmems_obs-oc_med_bgc-plankton_my_l4-olci-300m_P1M_202211",  # noqa: E501 cmems_obs-oc_med_bgc-plankton_my_l4-olci-300m_P1M
    "cmems_obs-oc_med_bgc-pp_my_l4-multi-4km_P1D_202311",  # noqa: E501 cmems_obs-oc_med_bgc-pp_my_l4-multi-4km_P1D
    "cmems_obs-oc_med_bgc-pp_my_l4-multi-4km_P1M_202311",  # noqa: E501 cmems_obs-oc_med_bgc-pp_my_l4-multi-4km_P1M
]


class oceancolour_med_bgc_l4_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_MED_BGC_L4_MY_009_144"
    dataset = "EO:MO:DAT:OCEANCOLOUR_MED_BGC_L4_MY_009_144"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "CHL",
            "CHL_count",
            "CHL_error",
            "PP",
            "PP_count",
            "PP_error",
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
        end_datetime="2024-06-07T00:00:00Z",
        start_datetime="1997-09-16T00:00:00Z",
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
