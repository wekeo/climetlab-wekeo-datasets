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
    "dataset-omega-3d-rep-weekly_202003",  # noqa: E501 Global observed ocean physics 3d quasi-geostrophic currents (omega3d)
]


class multiobs_glo_phy_w_3d_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_W_3D_REP_015_007"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_W_3D_REP_015_007"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "depth",
            "lat",
            "lon",
            "time",
            "uago",
            "uo",
            "vago",
            "vo",
            "wo",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="dataset-omega-3d-rep-weekly_202003",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "dataset-omega-3d-rep-weekly_202003":
            if start is None:
                start = "2020-03-31T00:00:00Z"

            if end is None:
                end = "2020-03-31T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
