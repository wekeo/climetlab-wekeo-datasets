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
    "MetO-NWS-WAV-RAN_202007",  # noqa: E501 MetO-NWS-WAV-RAN
]


class nwshelf_reanalysis_wav(Main):
    name = "EO:MO:DAT:NWSHELF_REANALYSIS_WAV_004_015"
    dataset = "EO:MO:DAT:NWSHELF_REANALYSIS_WAV_004_015"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
            "crs",
            "latitude",
            "longitude",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="MetO-NWS-WAV-RAN_202007",
        max_date="2023-12-31T00:00:00Z",
        min_date="1980-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "MetO-NWS-WAV-RAN_202007":
            if min_date is None:
                min_date = "1980-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-12-31T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
