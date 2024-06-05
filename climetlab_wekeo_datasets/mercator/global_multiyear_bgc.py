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
    "cmems_mod_glo_bgc_my_0.083deg-lmtl-Fphy_PT1D-i_202211",  # noqa: E501 cmems_mod_glo_bgc_my_0.083deg-lmtl-Fphy_PT1D-i
    "cmems_mod_glo_bgc_my_0.083deg-lmtl_PT1D-i_202211",  # noqa: E501 cmems_mod_glo_bgc_my_0.083deg-lmtl_PT1D-i
]


class global_multiyear_bgc(Main):
    name = "EO:MO:DAT:GLOBAL_MULTIYEAR_BGC_001_033"
    dataset = "EO:MO:DAT:GLOBAL_MULTIYEAR_BGC_001_033"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "T",
            "U",
            "V",
            "mnkc_epi",
            "mnkc_hmlmeso",
            "mnkc_lmeso",
            "mnkc_mlmeso",
            "mnkc_mumeso",
            "mnkc_umeso",
            "npp",
            "pelagic_layer_depth",
            "zeu",
            "zooc",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(self, layer, variables, bbox=None, limit=None):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
