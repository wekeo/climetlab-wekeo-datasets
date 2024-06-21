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
    "c3s_obs-oc_glo_bgc-plankton_my_l3-multi-4km_P1D_202303",  # noqa: E501 c3s_obs-oc_glo_bgc-plankton_my_l3-multi-4km_P1D
    "c3s_obs-oc_glo_bgc-reflectance_my_l3-multi-4km_P1D_202303",  # noqa: E501 c3s_obs-oc_glo_bgc-reflectance_my_l3-multi-4km_P1D
]


class oceancolour_glo_bgc_l3_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L3_MY_009_107"
    dataset = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L3_MY_009_107"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "CHL",
            "MICRO",
            "MICRO_BIAS",
            "MICRO_RMSE",
            "NANO",
            "NANO_BIAS",
            "NANO_RMSE",
            "PICO",
            "PICO_BIAS",
            "PICO_RMSE",
            "RRS412",
            "RRS443",
            "RRS490",
            "RRS510",
            "RRS560",
            "RRS665",
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
        end_datetime="2024-05-31T00:00:00Z",
        start_datetime="1997-09-04T00:00:00Z",
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
