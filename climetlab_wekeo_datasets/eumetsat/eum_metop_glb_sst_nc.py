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

    @normalize("bbox", "bounding-box(list)")
    @normalize("dtstart", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("dtend", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("publication", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
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
        bbox=None,
        dtstart=None,
        dtend=None,
        publication=None,
        sat="Metop-B",
        type="OSSTGLBN",
        limit=None,
    ):
        super().__init__(
            bbox=bbox,
            dtstart=dtstart,
            dtend=dtend,
            publication=publication,
            sat=sat,
            type=type,
            limit=limit,
        )
