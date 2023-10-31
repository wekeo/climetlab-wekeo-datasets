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
    "cmems_obs-mob_glo_phy-sss_my_multi-oi_P1W_202211",  # noqa: E501 cmems_obs-mob_glo_phy-sss_my_multi-oi_P1W_202211
]


class multiobs_glo_phy_sss_l4_my(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_SSS_L4_MY_015_015"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_SSS_L4_MY_015_015"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "CT",
            "SA",
            "alpha",
            "beta",
            "ice_mask",
            "lat",
            "lon",
            "rho",
            "spiciness0",
            "sss",
            "sss_corr_smos",
            "sss_isas",
            "sst",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-mob_glo_phy-sss_my_multi-oi_P1W_202211",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-mob_glo_phy-sss_my_multi-oi_P1W_202211":
            if start is None:
                start = "2011-01-02T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
