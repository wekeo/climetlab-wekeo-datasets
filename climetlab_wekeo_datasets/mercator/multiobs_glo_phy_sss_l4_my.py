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
    "cmems_obs-mob_glo_phy-sss_my_multi-oi_P1W_202406",  # noqa: E501 cmems_obs-mob_glo_phy-sss_my_multi-oi_P1W
]


class multiobs_glo_phy_sss_l4_my(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_SSS_L4_MY_015_015"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_SSS_L4_MY_015_015"

    @normalize(
        "variables",
        [
            "CT",
            "SA",
            "alpha",
            "beta",
            "ice_mask",
            "rho",
            "spiciness0",
            "sss",
            "sss_corr_smap",
            "sss_corr_smos",
            "sss_isas",
            "sst",
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        variables,
        layer="cmems_obs-mob_glo_phy-sss_my_multi-oi_P1W_202406",
        bbox=None,
        end_datetime="2023-12-21T00:00:00Z",
        start_datetime="2010-06-03T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            variables=variables,
            layer=layer,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
