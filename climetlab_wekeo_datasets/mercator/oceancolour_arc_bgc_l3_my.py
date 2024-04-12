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
    "cmems_obs-oc_arc_bgc-plankton_my_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_arc_bgc-plankton_my_l3-olci-300m_P1D_202303
    "cmems_obs-oc_arc_bgc-reflectance_my_l3-multi-4km_P1D_202311",  # noqa: E501 cmems_obs-oc_arc_bgc-reflectance_my_l3-multi-4km_P1D
    "cmems_obs-oc_arc_bgc-reflectance_my_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_arc_bgc-reflectance_my_l3-olci-300m_P1D_202303
    "cmems_obs-oc_arc_bgc-transp_my_l3-multi-4km_P1D_202311",  # noqa: E501 cmems_obs-oc_arc_bgc-transp_my_l3-multi-4km_P1D
    "cmems_obs-oc_arc_bgc-transp_my_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_arc_bgc-transp_my_l3-olci-300m_P1D_202303
]


class oceancolour_arc_bgc_l3_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_L3_MY_009_123"
    dataset = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_L3_MY_009_123"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
            "RRS400",
            "RRS412",
            "RRS412_5",
            "RRS442_5",
            "RRS443",
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
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-03-25T12:00:00Z",
        min_date="2016-04-26T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-oc_arc_bgc-plankton_my_l3-multi-4km_P1D_202311":
            if min_date is None:
                min_date = "1997-09-04T00:00:00Z"

            if max_date is None:
                max_date = "2023-12-31T00:00:00Z"

        if layer == "cmems_obs-oc_arc_bgc-plankton_my_l3-olci-300m_P1D_202303":
            if min_date is None:
                min_date = "2016-04-26T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-25T00:00:00Z"

        if layer == "cmems_obs-oc_arc_bgc-reflectance_my_l3-multi-4km_P1D_202311":
            if min_date is None:
                min_date = "1997-09-04T00:00:00Z"

            if max_date is None:
                max_date = "2034-12-31T00:00:00Z"

        if layer == "cmems_obs-oc_arc_bgc-reflectance_my_l3-olci-300m_P1D_202303":
            if min_date is None:
                min_date = "2016-04-26T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-25T12:00:00Z"

        if layer == "cmems_obs-oc_arc_bgc-transp_my_l3-multi-4km_P1D_202311":
            if min_date is None:
                min_date = "1997-09-04T00:00:00Z"

            if max_date is None:
                max_date = "2023-12-31T00:00:00Z"

        if layer == "cmems_obs-oc_arc_bgc-transp_my_l3-olci-300m_P1D_202303":
            if min_date is None:
                min_date = "2016-04-26T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-25T12:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
