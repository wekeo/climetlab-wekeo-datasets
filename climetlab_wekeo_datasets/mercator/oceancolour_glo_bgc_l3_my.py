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

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
            "latitude",
            "longitude",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-03-31T00:00:00Z",
        min_date="1997-09-04T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "c3s_obs-oc_glo_bgc-plankton_my_l3-multi-4km_P1D_202303":
            if min_date is None:
                min_date = "1997-09-04T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-31T00:00:00Z"

        if layer == "c3s_obs-oc_glo_bgc-reflectance_my_l3-multi-4km_P1D_202303":
            if min_date is None:
                min_date = "1997-09-04T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-31T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
