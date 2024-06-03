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
    "dataset-omega-3d-rep-weekly_202003",  # noqa: E501 dataset-omega-3d-rep-weekly
]


class multiobs_glo_phy_w_3d_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_W_3D_REP_015_007"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_W_3D_REP_015_007"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        bbox,
        layer="dataset-omega-3d-rep-weekly_202003",
        max_date="2020-03-31T00:00:00Z",
        min_date="2020-03-31T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "dataset-omega-3d-rep-weekly_202003":
            if min_date is None:
                min_date = "2020-03-31T00:00:00Z"

            if max_date is None:
                max_date = "2020-03-31T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
