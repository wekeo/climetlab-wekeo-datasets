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
    "cmems_obs-ins_glo_phy-cur_my_argo_irr_202311",  # noqa: E501 cmems_obs-ins_glo_phy-cur_my_argo_irr_202311
    "cmems_obs-ins_glo_phy-cur_my_drifter_PT6H_202311",  # noqa: E501 cmems_obs-ins_glo_phy-cur_my_drifter_PT6H_202311
]


class insitu_glo_phy_uv_discrete_my(Main):
    name = "EO:MO:DAT:INSITU_GLO_PHY_UV_DISCRETE_MY_013_044"
    dataset = "EO:MO:DAT:INSITU_GLO_PHY_UV_DISCRETE_MY_013_044"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "EWCT",
            "NSCT",
            "TEMP",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(self, layer, variables, bbox=None, limit=None):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
