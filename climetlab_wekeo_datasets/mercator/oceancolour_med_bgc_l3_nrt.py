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
    "cmems_obs-oc_med_bgc-optics_nrt_l3-multi-1km_P1D_202207",  # noqa: E501 cmems_obs-oc_med_bgc-optics_nrt_l3-multi-1km_P1D
    "cmems_obs-oc_med_bgc-plankton_nrt_l3-multi-1km_P1D_202211",  # noqa: E501 cmems_obs-oc_med_bgc-plankton_nrt_l3-multi-1km_P1D
    "cmems_obs-oc_med_bgc-plankton_nrt_l3-olci-300m_P1D_202207",  # noqa: E501 cmems_obs-oc_med_bgc-plankton_nrt_l3-olci-300m_P1D
    "cmems_obs-oc_med_bgc-reflectance_nrt_l3-multi-1km_P1D_202207",  # noqa: E501 cmems_obs-oc_med_bgc-reflectance_nrt_l3-multi-1km_P1D
    "cmems_obs-oc_med_bgc-reflectance_nrt_l3-olci-300m_P1D_202207",  # noqa: E501 cmems_obs-oc_med_bgc-reflectance_nrt_l3-olci-300m_P1D
    "cmems_obs-oc_med_bgc-transp_nrt_l3-multi-1km_P1D_202207",  # noqa: E501 cmems_obs-oc_med_bgc-transp_nrt_l3-multi-1km_P1D
    "cmems_obs-oc_med_bgc-transp_nrt_l3-olci-300m_P1D_202207",  # noqa: E501 cmems_obs-oc_med_bgc-transp_nrt_l3-olci-300m_P1D
]


class oceancolour_med_bgc_l3_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_MED_BGC_L3_NRT_009_141"
    dataset = "EO:MO:DAT:OCEANCOLOUR_MED_BGC_L3_NRT_009_141"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "ADG443",
            "APH443",
            "BBP443",
            "CHL",
            "CRYPTO",
            "DIATO",
            "DINO",
            "GREEN",
            "HAPTO",
            "KD490",
            "MICRO",
            "NANO",
            "PICO",
            "PROKAR",
            "QI_ADG443",
            "QI_APH443",
            "QI_BBP443",
            "QI_CHL",
            "QI_KD490",
            "QI_RRS412",
            "QI_RRS412_5",
            "QI_RRS442_5",
            "QI_RRS443",
            "QI_RRS490",
            "QI_RRS510",
            "QI_RRS555",
            "QI_RRS560",
            "QI_RRS670",
            "QI_RRS673_75",
            "RRS400",
            "RRS412",
            "RRS412_5",
            "RRS442_5",
            "RRS443",
            "RRS490",
            "RRS510",
            "RRS555",
            "RRS560",
            "RRS620",
            "RRS665",
            "RRS670",
            "RRS673_75",
            "RRS681_25",
            "RRS708_75",
            "RRS778_75",
            "RRS865",
            "SENSORMASK",
            "WTM",
            "lat",
            "lon",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-05-05T00:00:00Z",
        min_date="2023-12-03T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-oc_med_bgc-optics_nrt_l3-multi-1km_P1D_202207":
            if min_date is None:
                min_date = "2023-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs-oc_med_bgc-plankton_nrt_l3-multi-1km_P1D_202211":
            if min_date is None:
                min_date = "2023-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs-oc_med_bgc-plankton_nrt_l3-olci-300m_P1D_202207":
            if min_date is None:
                min_date = "2023-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs-oc_med_bgc-reflectance_nrt_l3-multi-1km_P1D_202207":
            if min_date is None:
                min_date = "2023-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs-oc_med_bgc-reflectance_nrt_l3-olci-300m_P1D_202207":
            if min_date is None:
                min_date = "2023-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs-oc_med_bgc-transp_nrt_l3-multi-1km_P1D_202207":
            if min_date is None:
                min_date = "2023-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs-oc_med_bgc-transp_nrt_l3-olci-300m_P1D_202207":
            if min_date is None:
                min_date = "2023-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
