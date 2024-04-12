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
    "cmems_obs-wind_glo_phy_nrt_l4_0.125deg_PT1H_202207",  # noqa: E501  global ocean - wind and stress - hourly - from scatterometer and model
    "cmems_obs-wind_glo_phy_nrt_l4_0.125deg_PT1H_202207",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l4_0.125deg_PT1H
]


class wind_glo_phy_l4_nrt(Main):
    name = "EO:MO:DAT:WIND_GLO_PHY_L4_NRT_012_004"
    dataset = "EO:MO:DAT:WIND_GLO_PHY_L4_NRT_012_004"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "air_density",
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
            "number_of_observations_divcurl",
            "stress_curl",
            "stress_curl_bias",
            "stress_curl_dv",
            "stress_divergence",
            "stress_divergence_bias",
            "stress_divergence_dv",
            "time",
            "wind_curl",
            "wind_curl_bias",
            "wind_curl_dv",
            "wind_divergence",
            "wind_divergence_bias",
            "wind_divergence_dv",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-03-18T23:00:00Z",
        min_date="2021-12-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-wind_glo_phy_nrt_l4_0.125deg_PT1H_202207":
            if min_date is None:
                min_date = "2021-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-18T23:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
