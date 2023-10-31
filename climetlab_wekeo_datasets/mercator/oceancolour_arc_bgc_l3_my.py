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
    "cmems_obs-oc_arc_bgc-plankton_my_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_arc_bgc-plankton_my_l3-olci-300m_P1D_202303
    "cmems_obs-oc_arc_bgc-reflectance_my_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_arc_bgc-reflectance_my_l3-olci-300m_P1D_202303
    "cmems_obs-oc_arc_bgc-transp_my_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_arc_bgc-transp_my_l3-olci-300m_P1D_202303
]


class oceancolour_arc_bgc_l3_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_L3_MY_009_123"
    dataset = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_L3_MY_009_123"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "CHL",
            "KD490",
            "RRS400",
            "RRS412_5",
            "RRS442_5",
            "RRS490",
            "RRS510",
            "RRS560",
            "RRS620",
            "RRS665",
            "RRS673_75",
            "RRS681_25",
            "RRS708_75",
            "SENSORMASK",
            "lat",
            "lon",
            "stereographic",
            "time",
            "x",
            "y",
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
        if layer == "cmems_obs-oc_arc_bgc-plankton_my_l3-olci-300m_P1D_202303":
            if start is None:
                start = "2016-04-26T00:00:00Z"

            if end is None:
                end = "2023-10-17T00:00:00Z"

        if layer == "cmems_obs-oc_arc_bgc-reflectance_my_l3-olci-300m_P1D_202303":
            if start is None:
                start = "2016-04-26T00:00:00Z"

            if end is None:
                end = "2023-10-17T00:00:00Z"

        if layer == "cmems_obs-oc_arc_bgc-transp_my_l3-olci-300m_P1D_202303":
            if start is None:
                start = "2016-04-26T00:00:00Z"

            if end is None:
                end = "2023-10-17T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
