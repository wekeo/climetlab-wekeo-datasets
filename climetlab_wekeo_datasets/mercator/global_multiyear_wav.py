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
    "cmems_mod_glo_wav_my_0.2_PT3H-i_202112",  # noqa: E501 Mean fields from global wave model mfwam of meteo-france with ecmwf forcing
]


class global_multiyear_wav(Main):
    name = "EO:MO:DAT:GLOBAL_MULTIYEAR_WAV_001_032"
    dataset = "EO:MO:DAT:GLOBAL_MULTIYEAR_WAV_001_032"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "VHM0",
            "VHM0_SW1",
            "VHM0_SW2",
            "VHM0_WW",
            "VMDR",
            "VMDR_SW1",
            "VMDR_SW2",
            "VMDR_WW",
            "VPED",
            "VSDX",
            "VSDY",
            "VTM01_SW1",
            "VTM01_SW2",
            "VTM01_WW",
            "VTM02",
            "VTM10",
            "VTPK",
            "latitude",
            "longitude",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_mod_glo_wav_my_0.2_PT3H-i_202112",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_mod_glo_wav_my_0.2_PT3H-i_202112":
            if start is None:
                start = "1993-01-01T00:00:00Z"

            if end is None:
                end = "2021-12-31T21:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
