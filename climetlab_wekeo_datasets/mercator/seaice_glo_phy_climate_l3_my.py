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
    "c3s_obs-si_glo_phy_my_nh-l3_P1M_202311",  # noqa: E501 c3s_obs-si_glo_phy_my_nh-l3_P1M
]


class seaice_glo_phy_climate_l3_my(Main):
    name = "EO:MO:DAT:SEAICE_GLO_PHY_CLIMATE_L3_MY_011_013"
    dataset = "EO:MO:DAT:SEAICE_GLO_PHY_CLIMATE_L3_MY_011_013"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "Lambert_Azimuthal_Grid",
            "lat",
            "lon",
            "quality_flag",
            "sea_ice_thickness",
            "status_flag",
            "time",
            "time_bnds",
            "uncertainty",
            "xc",
            "yc",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="c3s_obs-si_glo_phy_my_nh-l3_P1M_202311",
        max_date="2020-04-30T23:59:59Z",
        min_date="2002-10-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "c3s_obs-si_glo_phy_my_nh-l3_P1M_202311":
            if min_date is None:
                min_date = "2002-10-01T00:00:00Z"

            if max_date is None:
                max_date = "2020-04-30T23:59:59Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
