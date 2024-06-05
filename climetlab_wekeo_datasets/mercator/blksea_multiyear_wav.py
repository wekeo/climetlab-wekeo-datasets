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
    "cmems_mod_blk_wav_my_2.5km_PT1H-i_202311",  # noqa: E501 cmems_mod_blk_wav_my_2.5km_PT1H-i
    "cmems_mod_blk_wav_myint_2.5km_PT1H-i_202311",  # noqa: E501 cmems_mod_blk_wav_myint_2.5km_PT1H-i
]


class blksea_multiyear_wav(Main):
    name = "EO:MO:DAT:BLKSEA_MULTIYEAR_WAV_007_006"
    dataset = "EO:MO:DAT:BLKSEA_MULTIYEAR_WAV_007_006"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "VCMX",
            "VHM0",
            "VHM0_SW1",
            "VHM0_SW2",
            "VHM0_WW",
            "VMDR",
            "VMDR_SW1",
            "VMDR_SW2",
            "VMDR_WW",
            "VMXL",
            "VPED",
            "VSDX",
            "VSDY",
            "VTM01_SW1",
            "VTM01_SW2",
            "VTM01_WW",
            "VTM02",
            "VTM10",
            "VTPK",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(self, layer, variables, bbox=None, limit=None):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
