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
    "cmems_obs-oc_arc_bgc-plankton_nrt_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_arc_bgc-plankton_nrt_l3-olci-300m_P1D_202303
    "cmems_obs-oc_arc_bgc-reflectance_nrt_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_arc_bgc-reflectance_nrt_l3-olci-300m_P1D_202303
    "cmems_obs-oc_arc_bgc-transp_nrt_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_arc_bgc-transp_nrt_l3-olci-300m_P1D_202303
]


class oceancolour_arc_bgc_l3_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_L3_NRT_009_121"
    dataset = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_L3_NRT_009_121"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-04-01T12:00:00Z",
        min_date="2023-12-03T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-oc_arc_bgc-plankton_nrt_l3-olci-300m_P1D_202303":
            if min_date is None:
                min_date = "2024-03-26T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T00:00:00Z"

        if layer == "cmems_obs-oc_arc_bgc-reflectance_nrt_l3-olci-300m_P1D_202303":
            if min_date is None:
                min_date = "2023-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "cmems_obs-oc_arc_bgc-transp_nrt_l3-olci-300m_P1D_202303":
            if min_date is None:
                min_date = "2023-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
