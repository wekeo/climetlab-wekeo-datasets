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
    "cmems_mod_glo_bgc-bio_anfc_0.25deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_bgc-bio_anfc_0.25deg_P1D-m
    "cmems_mod_glo_bgc-bio_anfc_0.25deg_P1M-m_202311",  # noqa: E501 cmems_mod_glo_bgc-bio_anfc_0.25deg_P1M-m
    "cmems_mod_glo_bgc-car_anfc_0.25deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_bgc-car_anfc_0.25deg_P1D-m
    "cmems_mod_glo_bgc-car_anfc_0.25deg_P1M-m_202311",  # noqa: E501 cmems_mod_glo_bgc-car_anfc_0.25deg_P1M-m
    "cmems_mod_glo_bgc-co2_anfc_0.25deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_bgc-co2_anfc_0.25deg_P1D-m
    "cmems_mod_glo_bgc-co2_anfc_0.25deg_P1M-m_202311",  # noqa: E501 cmems_mod_glo_bgc-co2_anfc_0.25deg_P1M-m
    "cmems_mod_glo_bgc-nut_anfc_0.25deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_bgc-nut_anfc_0.25deg_P1D-m
    "cmems_mod_glo_bgc-nut_anfc_0.25deg_P1M-m_202311",  # noqa: E501 cmems_mod_glo_bgc-nut_anfc_0.25deg_P1M-m
    "cmems_mod_glo_bgc-optics_anfc_0.25deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_bgc-optics_anfc_0.25deg_P1D-m
    "cmems_mod_glo_bgc-pft_anfc_0.25deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_bgc-pft_anfc_0.25deg_P1D-m
    "cmems_mod_glo_bgc-pft_anfc_0.25deg_P1M-m_202311",  # noqa: E501 cmems_mod_glo_bgc-pft_anfc_0.25deg_P1M-m
]


class global_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:GLOBAL_ANALYSISFORECAST_BGC_001_028"
    dataset = "EO:MO:DAT:GLOBAL_ANALYSISFORECAST_BGC_001_028"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "chl",
            "dissic",
            "fe",
            "kd",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "po4",
            "si",
            "spco2",
            "talk",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        end_datetime="2024-05-01T00:00:00Z",
        start_datetime="2021-10-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
