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
    "cmems_mod_nws_bgc-chl_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-chl_my_7km-3D_P1D-m
    "cmems_mod_nws_bgc-chl_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-chl_my_7km-3D_P1M-m
    "cmems_mod_nws_bgc-chl_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-chl_myint_7km-3D_P1M-m
    "cmems_mod_nws_bgc-kd_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-kd_my_7km-3D_P1D-m
    "cmems_mod_nws_bgc-kd_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-kd_my_7km-3D_P1M-m
    "cmems_mod_nws_bgc-kd_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-kd_myint_7km-3D_P1M-m
    "cmems_mod_nws_bgc-no3_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-no3_my_7km-3D_P1D-m
    "cmems_mod_nws_bgc-no3_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-no3_my_7km-3D_P1M-m
    "cmems_mod_nws_bgc-no3_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-no3_myint_7km-3D_P1M-m
    "cmems_mod_nws_bgc-o2_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-o2_my_7km-3D_P1D-m
    "cmems_mod_nws_bgc-o2_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-o2_my_7km-3D_P1M-m
    "cmems_mod_nws_bgc-o2_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-o2_myint_7km-3D_P1M-m
    "cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1D-m
    "cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1M-m
    "cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1D-m
    "cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1M-m
    "cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1D-m
    "cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1M-m
    "cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1D-m
    "cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1M-m
    "cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m
    "cmems_mod_nws_bgc-pft_myint_7km-3D-dino_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-pft_myint_7km-3D-dino_P1M-m
    "cmems_mod_nws_bgc-pft_myint_7km-3D-nano_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-pft_myint_7km-3D-nano_P1M-m
    "cmems_mod_nws_bgc-pft_myint_7km-3D-pico_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-pft_myint_7km-3D-pico_P1M-m
    "cmems_mod_nws_bgc-ph_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-ph_my_7km-3D_P1D-m
    "cmems_mod_nws_bgc-ph_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-ph_my_7km-3D_P1M-m
    "cmems_mod_nws_bgc-ph_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-ph_myint_7km-3D_P1M-m
    "cmems_mod_nws_bgc-phyc_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-phyc_my_7km-3D_P1D-m
    "cmems_mod_nws_bgc-phyc_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-phyc_my_7km-3D_P1M-m
    "cmems_mod_nws_bgc-phyc_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-phyc_myint_7km-3D_P1M-m
    "cmems_mod_nws_bgc-po4_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-po4_my_7km-3D_P1D-m
    "cmems_mod_nws_bgc-po4_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-po4_my_7km-3D_P1M-m
    "cmems_mod_nws_bgc-po4_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-po4_myint_7km-3D_P1M-m
    "cmems_mod_nws_bgc-pp_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pp_my_7km-3D_P1D-m
    "cmems_mod_nws_bgc-pp_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-pp_my_7km-3D_P1M-m
    "cmems_mod_nws_bgc-pp_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-pp_myint_7km-3D_P1M-m
    "cmems_mod_nws_bgc-spco2_my_7km-2D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_bgc-spco2_my_7km-2D_P1D-m
    "cmems_mod_nws_bgc-spco2_my_7km-2D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_bgc-spco2_my_7km-2D_P1M-m
    "cmems_mod_nws_bgc-spco2_myint_7km-2D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_bgc-spco2_myint_7km-2D_P1M-m
]


class nwshelf_multiyear_bgc(Main):
    name = "EO:MO:DAT:NWSHELF_MULTIYEAR_BGC_004_011"
    dataset = "EO:MO:DAT:NWSHELF_MULTIYEAR_BGC_004_011"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "attn",
            "chl",
            "diato",
            "dino",
            "nano",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "pico",
            "po4",
            "spco2",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-3",
            "-10",
            "-15",
            "-20",
            "-30",
            "-50",
            "-75",
            "-100",
            "-125",
            "-150",
            "-200",
            "-250",
            "-300",
            "-400",
            "-500",
            "-600",
            "-750",
            "-1000",
            "-1500",
            "-2000",
            "-3000",
            "-4000",
            "-5000",
            "0",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-3",
            "-10",
            "-15",
            "-20",
            "-30",
            "-50",
            "-75",
            "-100",
            "-125",
            "-150",
            "-200",
            "-250",
            "-300",
            "-400",
            "-500",
            "-600",
            "-750",
            "-1000",
            "-1500",
            "-2000",
            "-3000",
            "-4000",
            "-5000",
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
        end_datetime="2023-08-31T00:00:00Z",
        start_datetime="1993-01-01T00:00:00Z",
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
