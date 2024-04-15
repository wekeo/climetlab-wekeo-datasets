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
    "cmems_obs-oc_atl_bgc-optics_nrt_l3-multi-1km_P1D_202311",  # noqa: E501 cmems_obs-oc_atl_bgc-optics_nrt_l3-multi-1km_P1D
    "cmems_obs-oc_atl_bgc-plankton_nrt_l3-multi-1km_P1D_202311",  # noqa: E501 cmems_obs-oc_atl_bgc-plankton_nrt_l3-multi-1km_P1D
    "cmems_obs-oc_atl_bgc-plankton_nrt_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_atl_bgc-plankton_nrt_l3-olci-300m_P1D
    "cmems_obs-oc_atl_bgc-reflectance_nrt_l3-multi-1km_P1D_202311",  # noqa: E501 cmems_obs-oc_atl_bgc-reflectance_nrt_l3-multi-1km_P1D
    "cmems_obs-oc_atl_bgc-reflectance_nrt_l3-olci-300m_P1D_202303",  # noqa: E501 cmems_obs-oc_atl_bgc-reflectance_nrt_l3-olci-300m_P1D
    "cmems_obs-oc_atl_bgc-transp_nrt_l3-multi-1km_P1D_202311",  # noqa: E501 cmems_obs-oc_atl_bgc-transp_nrt_l3-multi-1km_P1D
]


class oceancolour_atl_bgc_l3_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_ATL_BGC_L3_NRT_009_111"
    dataset = "EO:MO:DAT:OCEANCOLOUR_ATL_BGC_L3_NRT_009_111"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "BBP",
            "BBP_uncertainty",
            "CDM",
            "CDM_uncertainty",
            "CHL",
            "CHL_uncertainty",
            "DIATO",
            "DIATO_uncertainty",
            "DINO",
            "DINO_uncertainty",
            "GREEN",
            "GREEN_uncertainty",
            "HAPTO",
            "HAPTO_uncertainty",
            "KD490",
            "KD490_uncertainty",
            "MICRO",
            "MICRO_uncertainty",
            "NANO",
            "NANO_uncertainty",
            "PICO",
            "PICO_uncertainty",
            "PROCHLO",
            "PROCHLO_uncertainty",
            "PROKAR",
            "PROKAR_uncertainty",
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
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-04-01T00:00:00Z",
        min_date="2023-10-03T20:03:42Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-oc_atl_bgc-optics_nrt_l3-multi-1km_P1D_202311":
            if min_date is None:
                min_date = "2023-12-03T07:21:39Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        if layer == "cmems_obs-oc_atl_bgc-plankton_nrt_l3-multi-1km_P1D_202311":
            if min_date is None:
                min_date = "2023-12-03T07:21:39Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        if layer == "cmems_obs-oc_atl_bgc-plankton_nrt_l3-olci-300m_P1D_202303":
            if min_date is None:
                min_date = "2023-10-03T20:03:42Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        if layer == "cmems_obs-oc_atl_bgc-reflectance_nrt_l3-multi-1km_P1D_202311":
            if min_date is None:
                min_date = "2023-12-03T07:21:39Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        if layer == "cmems_obs-oc_atl_bgc-reflectance_nrt_l3-olci-300m_P1D_202303":
            if min_date is None:
                min_date = "2023-10-03T20:03:42Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        if layer == "cmems_obs-oc_atl_bgc-transp_nrt_l3-multi-1km_P1D_202311":
            if min_date is None:
                min_date = "2023-12-03T07:21:39Z"

            if max_date is None:
                max_date = "2024-04-01T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
