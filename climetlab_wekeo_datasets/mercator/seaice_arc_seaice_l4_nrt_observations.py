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
    "DMI-ARC-SEAICE_TEMP-L4-NRT-OBS",  # noqa: E501 DMI-ARC-SEAICE_TEMP-L4-NRT-OBS
]


class seaice_arc_seaice_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SEAICE_ARC_SEAICE_L4_NRT_OBSERVATIONS_011_008"
    dataset = "EO:MO:DAT:SEAICE_ARC_SEAICE_L4_NRT_OBSERVATIONS_011_008"

    @normalize(
        "variables",
        [
            "analysed_st",
            "analysis_error",
            "mask",
            "observation_max",
            "observation_min",
            "observation_num",
            "observation_std",
            "sea_ice_fraction",
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    def __init__(
        self, variables, layer="DMI-ARC-SEAICE_TEMP-L4-NRT-OBS", bbox=None, limit=None
    ):
        super().__init__(variables=variables, layer=layer, bbox=bbox, limit=limit)
