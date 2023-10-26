#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.eumetsat.main import Main


class eum_metop_glb_sst_nc(Main):
    name = "EO:EUM:DAT:METOP:GLB-SST-NC"
    dataset = "EO:EUM:DAT:METOP:GLB-SST-NC"
    inputs = [
        "relorbit",
        "orbit",
        "cycle",
    ]
    choices = [
        "sat",
        "type",
    ]

    @normalize("area", "bounding-box(list)")
    @normalize("relorbit")
    @normalize("orbit")
    @normalize("cycle")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "sat",
        [
            "Metop-B",
        ],
    )
    @normalize(
        "type",
        [
            "OSSTGLBN",
        ],
    )
    def __init__(
        self,
        area=None,
        relorbit=None,
        orbit=None,
        cycle=None,
        start="2016-07-11T05:58:03.000Z",
        end="2023-10-25T06:01:03.000Z",
        sat="Metop-B",
        type="OSSTGLBN",
    ):
        super().__init__(
            area=area,
            relorbit=relorbit,
            orbit=orbit,
            cycle=cycle,
            start=start,
            end=end,
            sat=sat,
            type=type,
        )
