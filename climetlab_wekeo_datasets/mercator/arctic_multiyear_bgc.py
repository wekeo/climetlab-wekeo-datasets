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
    "cmems_mod_arc_bgc_my_ecosmo_P1D-m_202105",  # noqa: E501 cmems_mod_arc_bgc_my_ecosmo_P1D-m
    "cmems_mod_arc_bgc_my_ecosmo_P1M_202105",  # noqa: E501 cmems_mod_arc_bgc_my_ecosmo_P1M
    "cmems_mod_arc_bgc_my_ecosmo_P1Y_202211",  # noqa: E501 cmems_mod_arc_bgc_my_ecosmo_P1Y
]


class arctic_multiyear_bgc(Main):
    name = "EO:MO:DAT:ARCTIC_MULTIYEAR_BGC_002_005"
    dataset = "EO:MO:DAT:ARCTIC_MULTIYEAR_BGC_002_005"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "chl",
            "kd",
            "model_depth",
            "no3",
            "nppv",
            "o2",
            "phyc",
            "po4",
            "si",
            "zooc",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(self, layer, variables, bbox=None, limit=None):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
