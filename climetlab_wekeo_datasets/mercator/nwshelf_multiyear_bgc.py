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
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "attn",
            "chl",
            "depth",
            "diato",
            "dino",
            "latitude",
            "longitude",
            "nano",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "pico",
            "po4",
            "spco2",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2023-08-16T12:00:00Z",
        min_date="1993-01-16T12:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_nws_bgc-chl_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-chl_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-chl_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-kd_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-kd_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-kd_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-no3_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-no3_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-no3_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-o2_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-o2_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-o2_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_myint_7km-3D-dino_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_myint_7km-3D-nano_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_myint_7km-3D-pico_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-ph_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-ph_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-ph_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-phyc_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-phyc_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-phyc_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-po4_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-po4_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-po4_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pp_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pp_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-pp_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-spco2_my_7km-2D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-spco2_my_7km-2D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_bgc-spco2_myint_7km-2D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
