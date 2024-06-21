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
    "c3s_obs-oc_glo_bgc-plankton_my_l4-multi-4km_P1M_202207",  # noqa: E501 c3s_obs-oc_glo_bgc-plankton_my_l4-multi-4km_P1M
]


class oceancolour_glo_bgc_l4_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_MY_009_108"
    dataset = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_MY_009_108"

    @normalize(
        "variables",
        [
            "CHL",
            "CHL_count",
            "CHL_error",
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
        layer="c3s_obs-oc_glo_bgc-plankton_my_l4-multi-4km_P1M_202207",
        bbox=None,
        end_datetime="2024-05-01T00:00:00Z",
        start_datetime="1997-09-01T00:00:00Z",
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
