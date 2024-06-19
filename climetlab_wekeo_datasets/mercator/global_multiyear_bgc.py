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
    @normalize(
        "maximum_depth",
        [
            "-1",
            "-2",
            "-3",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-1",
            "-2",
            "-3",
        ],
    )
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        maximum_depth=None,
        minimum_depth=None,
        end_datetime="2022-12-31T00:00:00Z",
        start_datetime="1998-01-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            maximum_depth=maximum_depth,
            minimum_depth=minimum_depth,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
