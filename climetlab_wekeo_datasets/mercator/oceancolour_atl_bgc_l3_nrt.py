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
        end_datetime="2024-06-18T00:00:00Z",
        start_datetime="2023-04-25T00:00:00Z",
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
