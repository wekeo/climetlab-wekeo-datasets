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
    "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-bio_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-bio_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-car_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-car_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202311",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m
    "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-nut_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-nut_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-opt_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-opt_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-pft_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-pft_anfc_3km_P1M-m
]


class blksea_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"
    dataset = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "chl",
            "dissic",
            "fpco2",
            "kd",
            "lght",
            "no3",
            "nppv",
            "o2",
            "o2b",
            "ph",
            "phyc",
            "po4",
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
        end_datetime="2024-02-01T00:00:00Z",
        start_datetime="2021-11-01T00:00:00Z",
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
