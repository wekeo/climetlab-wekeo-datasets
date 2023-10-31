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
    "cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1D-m_202211",  # noqa: E501 Biogeochemical 3d daily mean fields for the iberia-biscay-ireland (ibi) region
    "cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1M-m_202211",  # noqa: E501 Biogeochemical 3d monthly mean fields for the iberia-biscay-ireland (ibi) region
]


class ibi_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:IBI_ANALYSISFORECAST_BGC_005_004"
    dataset = "EO:MO:DAT:IBI_ANALYSISFORECAST_BGC_005_004"

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
            "fe",
            "latitude",
            "longitude",
            "nh4",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "po4",
            "si",
            "spco2",
            "time",
            "zeu",
            "zooc",
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
        if layer == "cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1D-m_202211":
            if start is None:
                start = "2021-10-25T00:00:00Z"

            if end is None:
                end = "2023-10-26T00:00:00Z"

        if layer == "cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1M-m_202211":
            if start is None:
                start = "2020-12-31T00:00:00Z"

            if end is None:
                end = "2023-09-30T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
