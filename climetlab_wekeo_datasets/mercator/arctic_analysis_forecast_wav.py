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
    "dataset-wam-arctic-1hr3km-be_201912",  # noqa: E501 Arctic ocean physics analysis and forecast
]


class arctic_analysis_forecast_wav(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSIS_FORECAST_WAV_002_014"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSIS_FORECAST_WAV_002_014"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "Current",
            "Currentdir",
            "SIC",
            "SIT",
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
            "depth",
            "forecast_reference_time",
            "lat",
            "lon",
            "projection_stere",
            "rlat",
            "rlon",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="dataset-wam-arctic-1hr3km-be_201912",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "dataset-wam-arctic-1hr3km-be_201912":
            if start is None:
                start = "2021-01-01T00:00:00Z"

            if end is None:
                end = "2023-11-03T12:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
