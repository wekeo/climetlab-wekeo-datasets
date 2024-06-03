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
    "cmems_obs-wind_glo_phy_my_l4_P1M_202211",  # noqa: E501 cmems_obs-wind_glo_phy_my_l4_P1M
]


class wind_glo_phy_climate_l4_my(Main):
    name = "EO:MO:DAT:WIND_GLO_PHY_CLIMATE_L4_MY_012_003"
    dataset = "EO:MO:DAT:WIND_GLO_PHY_CLIMATE_L4_MY_012_003"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "eastward_stress",
            "eastward_stress_bias",
            "eastward_stress_sdd",
            "eastward_wind",
            "eastward_wind_bias",
            "eastward_wind_sdd",
            "lat",
            "lon",
            "northward_stress",
            "northward_stress_bias",
            "northward_stress_sdd",
            "northward_wind",
            "northward_wind_bias",
            "northward_wind_sdd",
            "number_of_observations",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="cmems_obs-wind_glo_phy_my_l4_P1M_202211",
        max_date="2023-12-16T12:00:00Z",
        min_date="1999-08-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-wind_glo_phy_my_l4_P1M_202211":
            if min_date is None:
                min_date = "1999-08-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-12-16T12:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
