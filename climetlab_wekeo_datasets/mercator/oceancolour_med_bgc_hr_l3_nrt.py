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
    "cmems_obs_oc_med_bgc_geophy_nrt_l3-hr_P1D-m_202105",  # noqa: E501 cmems_obs_oc_med_bgc_geophy_nrt_l3-hr_P1D-m_202105
    "cmems_obs_oc_med_bgc_optics_nrt_l3-hr_P1D-m_202105",  # noqa: E501 cmems_obs_oc_med_bgc_optics_nrt_l3-hr_P1D-m_202105
    "cmems_obs_oc_med_bgc_transp_nrt_l3-hr_P1D-m_202105",  # noqa: E501 cmems_obs_oc_med_bgc_transp_nrt_l3-hr_P1D-m_202105
    "cmems_obs_oc_med_bgc_tur-spm-chl_nrt_l3-hr-mosaic_P1D-m_202107",  # noqa: E501 cmems_obs_oc_med_bgc_tur-spm-chl_nrt_l3-hr-mosaic_P1D-m
]


class oceancolour_med_bgc_hr_l3_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_MED_BGC_HR_L3_NRT_009_205"
    dataset = "EO:MO:DAT:OCEANCOLOUR_MED_BGC_HR_L3_NRT_009_205"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "BBP443",
            "BBP492",
            "BBP560",
            "BBP665",
            "BBP704",
            "BBP740",
            "BBP783",
            "BBP865",
            "CHL",
            "RRS443",
            "RRS443_UNC",
            "RRS492",
            "RRS492_UNC",
            "RRS560",
            "RRS560_UNC",
            "RRS665",
            "RRS665_UNC",
            "RRS704",
            "RRS704_UNC",
            "RRS740",
            "RRS740_UNC",
            "RRS783",
            "RRS783_UNC",
            "RRS865",
            "RRS865_UNC",
            "SPM",
            "SPM_QI",
            "TUR",
            "TUR_QI",
            "crs",
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
        min_date="2020-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs_oc_med_bgc_geophy_nrt_l3-hr_P1D-m_202105":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs_oc_med_bgc_optics_nrt_l3-hr_P1D-m_202105":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs_oc_med_bgc_transp_nrt_l3-hr_P1D-m_202105":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-05T00:00:00Z"

        if layer == "cmems_obs_oc_med_bgc_tur-spm-chl_nrt_l3-hr-mosaic_P1D-m_202107":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

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
