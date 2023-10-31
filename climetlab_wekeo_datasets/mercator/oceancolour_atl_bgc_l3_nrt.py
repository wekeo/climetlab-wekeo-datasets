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
    "cmems_obs-oc_atl_bgc-optics_nrt_l3-multi-1km_P1D_202303",  # noqa: E501 Cmems obs-oc atl bgc-optics NRT l3-multi-1km p1d
    "cmems_obs-oc_atl_bgc-plankton_nrt_l3-multi-1km_P1D_202303",  # noqa: E501 Cmems obs-oc atl bgc-plankton NRT l3-multi-1km p1d
    "cmems_obs-oc_atl_bgc-plankton_nrt_l3-olci-300m_P1D_202303",  # noqa: E501 Cmems obs-oc atl bgc-plankton NRT l3-olci-300m p1d
    "cmems_obs-oc_atl_bgc-reflectance_nrt_l3-multi-1km_P1D_202303",  # noqa: E501 Cmems obs-oc atl bgc-reflectance NRT l3-multi-1km p1d
    "cmems_obs-oc_atl_bgc-reflectance_nrt_l3-olci-300m_P1D_202303",  # noqa: E501 Cmems obs-oc atl bgc-reflectance NRT l3-olci-300m p1d
    "cmems_obs-oc_atl_bgc-transp_nrt_l3-multi-1km_P1D_202303",  # noqa: E501 Cmems obs-oc atl bgc-transp NRT l3-multi-1km p1d
]


class oceancolour_atl_bgc_l3_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_ATL_BGC_L3_NRT_009_111"
    dataset = "EO:MO:DAT:OCEANCOLOUR_ATL_BGC_L3_NRT_009_111"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "BBP",
            "BBP_uncertainty",
            "CDM",
            "CDM_uncertainty",
            "CHL",
            "CHL_uncertainty",
            "KD490",
            "KD490_uncertainty",
            "RRS400",
            "RRS400_uncertainty",
            "RRS412",
            "RRS412_uncertainty",
            "RRS443",
            "RRS443_uncertainty",
            "RRS490",
            "RRS490_uncertainty",
            "RRS510",
            "RRS510_uncertainty",
            "RRS555",
            "RRS555_uncertainty",
            "RRS560",
            "RRS560_uncertainty",
            "RRS620",
            "RRS620_uncertainty",
            "RRS670",
            "RRS670_uncertainty",
            "RRS674",
            "RRS674_uncertainty",
            "RRS681",
            "RRS681_uncertainty",
            "RRS709",
            "RRS709_uncertainty",
            "SPM",
            "SPM_uncertainty",
            "ZSD",
            "ZSD_uncertainty",
            "flags",
            "lat",
            "lon",
            "time",
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
        if layer == "cmems_obs-oc_atl_bgc-optics_nrt_l3-multi-1km_P1D_202303":
            if start is None:
                start = "2023-10-04T09:54:32Z"

            if end is None:
                end = "2023-10-27T16:54:59Z"

        if layer == "cmems_obs-oc_atl_bgc-plankton_nrt_l3-multi-1km_P1D_202303":
            if start is None:
                start = "2023-10-20T07:02:15Z"

            if end is None:
                end = "2023-10-27T17:11:59Z"

        if layer == "cmems_obs-oc_atl_bgc-plankton_nrt_l3-olci-300m_P1D_202303":
            if start is None:
                start = "2023-10-03T20:03:42Z"

            if end is None:
                end = "2023-10-27T22:33:15Z"

        if layer == "cmems_obs-oc_atl_bgc-reflectance_nrt_l3-multi-1km_P1D_202303":
            if start is None:
                start = "2023-10-04T09:54:32Z"

            if end is None:
                end = "2023-10-27T16:54:59Z"

        if layer == "cmems_obs-oc_atl_bgc-reflectance_nrt_l3-olci-300m_P1D_202303":
            if start is None:
                start = "2023-10-03T20:03:42Z"

            if end is None:
                end = "2023-10-27T22:33:15Z"

        if layer == "cmems_obs-oc_atl_bgc-transp_nrt_l3-multi-1km_P1D_202303":
            if start is None:
                start = "2023-10-20T07:02:15Z"

            if end is None:
                end = "2023-10-27T17:11:59Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
