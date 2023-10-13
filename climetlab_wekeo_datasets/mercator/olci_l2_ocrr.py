#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize
from climetlab_wekeo_sentinel3_level2.main import Main


class olci_l2_ocrr(Main):
    name = "EO:EUM:DAT:SENTINEL-3:0557"
    dataset = "EO:EUM:DAT:SENTINEL-3:0557"
    inputs = [
        "relorbit",
        "orbit",
        "cycle",
    ]
    choices = [
        "sat",
        "type",
        "timeliness",
    ]

    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "sat",
        [
            "Sentinel-3A",
            "Sentinel-3B",
        ],
    )
    @normalize(
        "type",
        [
            "OL_2_WRR___",
        ],
    )
    @normalize(
        "timeliness",
        [
            "NT",
        ],
    )
    @normalize("relorbit")
    @normalize("orbit")
    @normalize("cycle")
    def __init__(
        self,
        area=None,
        start="2016-04-25T11:33:13.903Z",
        end="2021-04-28T23:45:44.239Z",
        sat=None,
        type="OL_2_WRR___",
        timeliness="NT",
        relorbit=None,
        orbit=None,
        cycle=None,
    ):
        super().__init__(
            area=area,
            start=start,
            end=end,
            sat=sat,
            type=type,
            timeliness=timeliness,
            relorbit=relorbit,
            orbit=orbit,
            cycle=cycle,
        )
