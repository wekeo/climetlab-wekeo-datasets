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
    "cmems_mod_bal_bgc-pp_anfc_P1D-i_202211",  # noqa: E501 Cmems ergom accumulated daily npp
    "cmems_mod_bal_bgc_anfc_P1D-m_202211",  # noqa: E501 Cmems ergom daily integrated model fields
    "cmems_mod_bal_bgc_anfc_P1M-m_202211",  # noqa: E501 Cmems ergom monthly integrated model fields
]


class balticsea_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_BGC_003_007"
    dataset = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_BGC_003_007"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "dissic",
            "kd",
            "lat",
            "lon",
            "nh4",
            "no3",
            "nppv",
            "o2",
            "o2b",
            "pH",
            "phyc",
            "po4",
            "si",
            "spCO2",
            "time",
            "zooc",
            "zsd",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer,
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_mod_bal_bgc-pp_anfc_P1D-i_202211":
            if start is None:
                start = "2021-01-01T12:00:00Z"

            if end is None:
                end = "2023-11-01T12:00:00Z"

        if layer == "cmems_mod_bal_bgc_anfc_P1D-m_202211":
            if start is None:
                start = "2021-01-01T12:00:00Z"

            if end is None:
                end = "2023-11-01T12:00:00Z"

        if layer == "cmems_mod_bal_bgc_anfc_P1M-m_202211":
            if start is None:
                start = "2021-01-16T12:00:00Z"

            if end is None:
                end = "2023-09-16T06:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
