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
    "cmems_obs-oc_arc_bgc-plankton_my_l3-multi-4km_P1D_202311",  # noqa: E501 cmems_obs-oc_arc_bgc-plankton_my_l3-multi-4km_P1D
    "cmems_obs-oc_arc_bgc-reflectance_my_l3-multi-4km_P1D_202311",  # noqa: E501 cmems_obs-oc_arc_bgc-reflectance_my_l3-multi-4km_P1D
    "cmems_obs-oc_arc_bgc-transp_my_l3-multi-4km_P1D_202311",  # noqa: E501 cmems_obs-oc_arc_bgc-transp_my_l3-multi-4km_P1D
]


class oceancolour_arc_bgc_l3_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_L3_MY_009_123"
    dataset = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_L3_MY_009_123"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "CHL",
            "KD490",
            "QI_CHL",
            "QI_KD490",
            "QI_RRS412",
            "QI_RRS443",
            "QI_RRS490",
            "QI_RRS510",
            "QI_RRS560",
            "QI_RRS665",
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
        end_datetime="2023-12-31T00:00:00Z",
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
