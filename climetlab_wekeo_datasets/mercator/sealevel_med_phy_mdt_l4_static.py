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
    "cmems_obs-sl_med_phy-mdt_my_l4-0.0417deg_P20Y_202105",  # noqa: E501 cmems_obs-sl_med_phy-mdt_my_l4-0.0417deg_P20Y
]


class sealevel_med_phy_mdt_l4_static(Main):
    name = "EO:MO:DAT:SEALEVEL_MED_PHY_MDT_L4_STATIC_008_066"
    dataset = "EO:MO:DAT:SEALEVEL_MED_PHY_MDT_L4_STATIC_008_066"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "climatology_bnds",
            "crs",
            "err_mdt",
            "err_u",
            "err_v",
            "lat_bnds",
            "latitude",
            "lon_bnds",
            "longitude",
            "mdt",
            "nv",
            "time",
            "u",
            "v",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="cmems_obs-sl_med_phy-mdt_my_l4-0.0417deg_P20Y_202105",
        max_date="2013-01-01T00:00:00Z",
        min_date="1993-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-sl_med_phy-mdt_my_l4-0.0417deg_P20Y_202105":
            if min_date is None:
                min_date = "1993-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2013-01-01T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
