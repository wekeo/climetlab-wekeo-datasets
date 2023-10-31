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
    "cmems_obs-oc_glo_bgc-optics_my_l3-multi-4km_P1D_202207",  # noqa: E501 Cmems obs-oc glo bgc-optics my l3-multi-4km p1d
    "cmems_obs-oc_glo_bgc-plankton_my_l3-multi-4km_P1D_202207",  # noqa: E501 Cmems obs-oc glo bgc-plankton my l3-multi-4km p1d
    "cmems_obs-oc_glo_bgc-plankton_my_l3-olci-300m_P1D_202211",  # noqa: E501 Cmems obs-oc glo bgc-plankton my l3-olci-300m p1d
    "cmems_obs-oc_glo_bgc-plankton_my_l3-olci-4km_P1D_202207",  # noqa: E501 Cmems obs-oc glo bgc-plankton my l3-olci-4km p1d
    "cmems_obs-oc_glo_bgc-reflectance_my_l3-multi-4km_P1D_202207",  # noqa: E501 Cmems obs-oc glo bgc-reflectance my l3-multi-4km p1d
    "cmems_obs-oc_glo_bgc-reflectance_my_l3-olci-300m_P1D_202211",  # noqa: E501 Cmems obs-oc glo bgc-reflectance my l3-olci-300m p1d
    "cmems_obs-oc_glo_bgc-reflectance_my_l3-olci-4km_P1D_202207",  # noqa: E501 Cmems obs-oc glo bgc-reflectance my l3-olci-4km p1d
    "cmems_obs-oc_glo_bgc-transp_my_l3-multi-4km_P1D_202207",  # noqa: E501 Cmems obs-oc glo bgc-transp my l3-multi-4km p1d
    "cmems_obs-oc_glo_bgc-transp_my_l3-olci-4km_P1D_202207",  # noqa: E501 Cmems obs-oc glo bgc-transp my l3-olci-4km p1d
]


class oceancolour_glo_bgc_l3_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L3_MY_009_103"
    dataset = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L3_MY_009_103"

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
        if layer == "cmems_obs-oc_glo_bgc-optics_my_l3-multi-4km_P1D_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-10-18T03:33:04Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_my_l3-multi-4km_P1D_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-10-18T04:12:00Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_my_l3-olci-300m_P1D_202211":
            if start is None:
                start = "2016-04-25T11:40:53Z"

            if end is None:
                end = "2023-10-17T23:26:59Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_my_l3-olci-4km_P1D_202207":
            if start is None:
                start = "2016-04-25T11:34:53Z"

            if end is None:
                end = "2023-10-18T23:03:27Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_my_l3-multi-4km_P1D_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-10-18T03:33:04Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_my_l3-olci-300m_P1D_202211":
            if start is None:
                start = "2016-04-25T11:40:53Z"

            if end is None:
                end = "2023-10-17T23:26:59Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_my_l3-olci-4km_P1D_202207":
            if start is None:
                start = "2016-04-25T11:34:53Z"

            if end is None:
                end = "2023-10-18T23:03:27Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_my_l3-multi-4km_P1D_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-10-18T04:12:00Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_my_l3-olci-4km_P1D_202207":
            if start is None:
                start = "2016-04-25T11:34:53Z"

            if end is None:
                end = "2023-10-18T23:03:27Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
