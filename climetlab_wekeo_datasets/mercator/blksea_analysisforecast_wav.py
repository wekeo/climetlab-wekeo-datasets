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
    "cmems_mod_blk_wav_anfc_2.5km_PT1H-i_202311",  # noqa: E501 cmems_mod_blk_wav_anfc_2.5km_PT1H-i
    "cmems_mod_blk_wav_anfc_2.5km_static_202112",  # noqa: E501 cmems_mod_blk_wav_anfc_2.5km_static
]


class blksea_analysisforecast_wav(Main):
    name = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_WAV_007_003"
    dataset = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_WAV_007_003"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
            "e1t",
            "e2t",
            "lat",
            "latitude",
            "lon",
            "longitude",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2021-12-28T00:00:00Z",
        min_date="2021-12-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_blk_wav_anfc_2.5km_PT1H-i_202311":
            if min_date is None:
                min_date = "2022-01-24T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T11:00:00Z"

        if layer == "cmems_mod_blk_wav_anfc_2.5km_static_202112":
            if min_date is None:
                min_date = "2021-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2021-12-28T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
