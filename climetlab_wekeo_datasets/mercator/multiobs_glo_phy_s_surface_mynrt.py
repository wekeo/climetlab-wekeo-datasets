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
    "cmems_obs-mob_glo_phy-sss_my_multi_P1D_202311",  # noqa: E501 cmems_obs-mob_glo_phy-sss_my_multi_P1D
    "cmems_obs-mob_glo_phy-sss_my_multi_P1M_202311",  # noqa: E501 cmems_obs-mob_glo_phy-sss_my_multi_P1M
    "cmems_obs-mob_glo_phy-sss_nrt_multi_P1D_202311",  # noqa: E501 cmems_obs-mob_glo_phy-sss_nrt_multi_P1D
    "cmems_obs-mob_glo_phy-sss_nrt_multi_P1M_202311",  # noqa: E501 cmems_obs-mob_glo_phy-sss_nrt_multi_P1M
]


class multiobs_glo_phy_s_surface_mynrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "dos",
            "dos_error",
            "sea_ice_fraction",
            "sos",
            "sos_error",
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
        start_datetime="2021-01-01T00:00:00Z",
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
