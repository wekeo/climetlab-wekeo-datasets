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
    "cmems_obs_mob_glo_phy-cur_my_0.25deg_P1D-m_202311",  # noqa: E501 cmems_obs_mob_glo_phy-cur_my_0.25deg_P1D-m
    "cmems_obs_mob_glo_phy-cur_my_0.25deg_P1M-m_202311",  # noqa: E501 cmems_obs_mob_glo_phy-cur_my_0.25deg_P1M-m
    "cmems_obs_mob_glo_phy-cur_my_0.25deg_PT1H-i_202311",  # noqa: E501 cmems_obs_mob_glo_phy-cur_my_0.25deg_PT1H-i
    "cmems_obs_mob_glo_phy-cur_nrt_0.25deg_P1D-m_202311",  # noqa: E501 cmems_obs_mob_glo_phy-cur_nrt_0.25deg_P1D-m
    "cmems_obs_mob_glo_phy-cur_nrt_0.25deg_P1M-m_202311",  # noqa: E501 cmems_obs_mob_glo_phy-cur_nrt_0.25deg_P1M-m
    "cmems_obs_mob_glo_phy-cur_nrt_0.25deg_PT1H-i_202311",  # noqa: E501 cmems_obs_mob_glo_phy-cur_nrt_0.25deg_PT1H-i
]


class multiobs_glo_phy_mynrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_MYNRT_015_003"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_MYNRT_015_003"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "crs",
            "depth",
            "err_ue",
            "err_ugos",
            "err_uo",
            "err_ve",
            "err_vgos",
            "err_vo",
            "latitude",
            "longitude",
            "time",
            "ue",
            "ugos",
            "uo",
            "ve",
            "vgos",
            "vo",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-04-01T12:00:00Z",
        min_date="2022-01-01T12:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs_mob_glo_phy-cur_my_0.25deg_P1D-m_202311":
            if min_date is None:
                min_date = "2023-07-25T00:00:00Z"

            if max_date is None:
                max_date = "2023-09-28T00:00:00Z"

        if layer == "cmems_obs_mob_glo_phy-cur_my_0.25deg_P1M-m_202311":
            if min_date is None:
                min_date = "2023-07-25T00:00:00Z"

            if max_date is None:
                max_date = "2023-09-28T00:00:00Z"

        if layer == "cmems_obs_mob_glo_phy-cur_my_0.25deg_PT1H-i_202311":
            if min_date is None:
                min_date = "2023-07-25T00:00:00Z"

            if max_date is None:
                max_date = "2023-09-28T00:00:00Z"

        if layer == "cmems_obs_mob_glo_phy-cur_nrt_0.25deg_P1D-m_202311":
            if min_date is None:
                min_date = "2022-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "cmems_obs_mob_glo_phy-cur_nrt_0.25deg_P1M-m_202311":
            if min_date is None:
                min_date = "2022-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_obs_mob_glo_phy-cur_nrt_0.25deg_PT1H-i_202311":
            if min_date is None:
                min_date = "2022-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T23:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
