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
    "cmems_obs_oc_nws_bgc_geophy_nrt_l4-hr_P1D-m_202105",  # noqa: E501 cmems_obs_oc_nws_bgc_geophy_nrt_l4-hr_P1D-m_202105
    "cmems_obs_oc_nws_bgc_geophy_nrt_l4-hr_P1M-m_202105",  # noqa: E501 cmems_obs_oc_nws_bgc_geophy_nrt_l4-hr_P1M-m_202105
    "cmems_obs_oc_nws_bgc_optics_nrt_l4-hr_P1D-m_202105",  # noqa: E501 cmems_obs_oc_nws_bgc_optics_nrt_l4-hr_P1D-m_202105
    "cmems_obs_oc_nws_bgc_optics_nrt_l4-hr_P1M-m_202105",  # noqa: E501 cmems_obs_oc_nws_bgc_optics_nrt_l4-hr_P1M-m_202105
    "cmems_obs_oc_nws_bgc_transp_nrt_l4-hr_P1D-m_202105",  # noqa: E501 cmems_obs_oc_nws_bgc_transp_nrt_l4-hr_P1D-m_202105
    "cmems_obs_oc_nws_bgc_transp_nrt_l4-hr_P1M-m_202105",  # noqa: E501 cmems_obs_oc_nws_bgc_transp_nrt_l4-hr_P1M-m_202105
    "cmems_obs_oc_nws_bgc_tur-spm-chl_nrt_l4-hr-mosaic_P1D-m_202107",  # noqa: E501 cmems_obs_oc_nws_bgc_tur-spm-chl_nrt_l4-hr-mosaic_P1D-m
]


class oceancolour_nws_bgc_hr_l4_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_NWS_BGC_HR_L4_NRT_009_209"
    dataset = "EO:MO:DAT:OCEANCOLOUR_NWS_BGC_HR_L4_NRT_009_209"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "BBP443",
            "BBP443_count",
            "BBP443_error",
            "CHL",
            "CHL_count",
            "CHL_error",
            "SPM",
            "SPM_count",
            "SPM_error",
            "TUR",
            "TUR_count",
            "TUR_error",
            "crs",
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
        max_date="2024-02-01T00:00:00Z",
        min_date="2020-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs_oc_nws_bgc_geophy_nrt_l4-hr_P1D-m_202105":
            if min_date is None:
                min_date = "2020-01-04T00:00:00Z"

            if max_date is None:
                max_date = "2023-12-28T00:00:00Z"

        if layer == "cmems_obs_oc_nws_bgc_geophy_nrt_l4-hr_P1M-m_202105":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_obs_oc_nws_bgc_optics_nrt_l4-hr_P1D-m_202105":
            if min_date is None:
                min_date = "2020-01-04T00:00:00Z"

            if max_date is None:
                max_date = "2023-12-28T00:00:00Z"

        if layer == "cmems_obs_oc_nws_bgc_optics_nrt_l4-hr_P1M-m_202105":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_obs_oc_nws_bgc_transp_nrt_l4-hr_P1D-m_202105":
            if min_date is None:
                min_date = "2020-01-04T00:00:00Z"

            if max_date is None:
                max_date = "2023-12-28T00:00:00Z"

        if layer == "cmems_obs_oc_nws_bgc_transp_nrt_l4-hr_P1M-m_202105":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_obs_oc_nws_bgc_tur-spm-chl_nrt_l4-hr-mosaic_P1D-m_202107":
            if min_date is None:
                min_date = "2020-01-04T00:00:00Z"

            if max_date is None:
                max_date = "2023-10-31T23:59:59Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
