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
    "cmems_obs-oc_glo_bgc-optics_nrt_l4-multi-4km_P1M_202311",  # noqa: E501 cmems_obs-oc_glo_bgc-optics_nrt_l4-multi-4km_P1M
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-gapfree-multi-4km_P1D_202311",  # noqa: E501 cmems_obs-oc_glo_bgc-plankton_nrt_l4-gapfree-multi-4km_P1D
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-multi-4km_P1M_202311",  # noqa: E501 cmems_obs-oc_glo_bgc-plankton_nrt_l4-multi-4km_P1M
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-300m_P1M_202211",  # noqa: E501 cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-300m_P1M
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-4km_P1M_202207",  # noqa: E501 cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-4km_P1M
    "cmems_obs-oc_glo_bgc-pp_nrt_l4-multi-4km_P1M_202311",  # noqa: E501 cmems_obs-oc_glo_bgc-pp_nrt_l4-multi-4km_P1M
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-multi-4km_P1M_202311",  # noqa: E501 cmems_obs-oc_glo_bgc-reflectance_nrt_l4-multi-4km_P1M
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-300m_P1M_202211",  # noqa: E501 cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-300m_P1M
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-4km_P1M_202207",  # noqa: E501 cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-4km_P1M
    "cmems_obs-oc_glo_bgc-transp_nrt_l4-gapfree-multi-4km_P1D_202311",  # noqa: E501 cmems_obs-oc_glo_bgc-transp_nrt_l4-gapfree-multi-4km_P1D
    "cmems_obs-oc_glo_bgc-transp_nrt_l4-multi-4km_P1M_202311",  # noqa: E501 cmems_obs-oc_glo_bgc-transp_nrt_l4-multi-4km_P1M
    "cmems_obs-oc_glo_bgc-transp_nrt_l4-olci-4km_P1M_202207",  # noqa: E501 cmems_obs-oc_glo_bgc-transp_nrt_l4-olci-4km_P1M
]


class oceancolour_glo_bgc_l4_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_NRT_009_102"
    dataset = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_NRT_009_102"

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
            "PP",
            "PP_uncertainty",
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
            "RRS665",
            "RRS665_uncertainty",
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
        end_datetime="2024-05-01T00:00:00Z",
        start_datetime="2023-04-01T00:00:00Z",
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
