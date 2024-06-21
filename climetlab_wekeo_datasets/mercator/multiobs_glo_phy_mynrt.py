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
    @normalize(
        "variables",
        [
            "err_ue",
            "err_ugos",
            "err_uo",
            "err_ve",
            "err_vgos",
            "err_vo",
            "ue",
            "ugos",
            "uo",
            "ve",
            "vgos",
            "vo",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-15",
            "0",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-15",
            "0",
        ],
    )
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        maximum_depth=None,
        minimum_depth=None,
        end_datetime="2023-12-31T00:00:00Z",
        start_datetime="1993-01-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            maximum_depth=maximum_depth,
            minimum_depth=minimum_depth,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
