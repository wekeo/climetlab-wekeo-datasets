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
    "cmems_mod_arc_bgc_anfc_ecosmo_P1D-m_202105",  # noqa: E501 cmems_mod_arc_bgc_anfc_ecosmo_P1D-m
    "cmems_mod_arc_bgc_anfc_ecosmo_P1M-m_202211",  # noqa: E501 cmems_mod_arc_bgc_anfc_ecosmo_P1M-m
]


class arctic_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_BGC_002_004"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_BGC_002_004"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "chl",
            "dissic",
            "expc",
            "kd",
            "model_depth",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "po4",
            "si",
            "spco2",
            "zooc",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-2",
            "-3",
            "-4",
            "-5",
            "-6",
            "-8",
            "-10",
            "-11",
            "-13",
            "-16",
            "-18",
            "-22",
            "-25",
            "-29",
            "-34",
            "-40",
            "-47",
            "-56",
            "-66",
            "-78",
            "-92",
            "-110",
            "-131",
            "-156",
            "-186",
            "-222",
            "-266",
            "-318",
            "-380",
            "-454",
            "-541",
            "-644",
            "-763",
            "-902",
            "-1062",
            "-2000",
            "-3000",
            "-3500",
            "-4000",
            "0",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-2",
            "-3",
            "-4",
            "-5",
            "-6",
            "-8",
            "-10",
            "-11",
            "-13",
            "-16",
            "-18",
            "-22",
            "-25",
            "-29",
            "-34",
            "-40",
            "-47",
            "-56",
            "-66",
            "-78",
            "-92",
            "-110",
            "-131",
            "-156",
            "-186",
            "-222",
            "-266",
            "-318",
            "-380",
            "-454",
            "-541",
            "-644",
            "-763",
            "-902",
            "-1062",
            "-2000",
            "-3000",
            "-3500",
            "-4000",
            "0",
        ],
    )
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        maximum_depth=None,
        minimum_depth=None,
        end_datetime="2024-06-27T00:00:00Z",
        start_datetime="2019-03-22T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            maximum_depth=maximum_depth,
            minimum_depth=minimum_depth,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
