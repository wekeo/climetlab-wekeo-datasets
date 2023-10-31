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
    "cmems_mod_nws_bgc-chl_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean chlorophyll concentration (3d)
    "cmems_mod_nws_bgc-chl_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean chlorophyll concentration (3d)
    "cmems_mod_nws_bgc-chl_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean chlorophyll concentration (3d)
    "cmems_mod_nws_bgc-kd_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean attenuation coefficient (3d)
    "cmems_mod_nws_bgc-kd_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean attenuation coefficient (3d)
    "cmems_mod_nws_bgc-kd_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean attenuation coefficient (3d)
    "cmems_mod_nws_bgc-no3_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean nitrate (3d)
    "cmems_mod_nws_bgc-no3_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean nitrate (3d)
    "cmems_mod_nws_bgc-no3_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean nitrate (3d)
    "cmems_mod_nws_bgc-o2_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean dissolved oxygen (3d)
    "cmems_mod_nws_bgc-o2_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean dissolved oxygen (3d)
    "cmems_mod_nws_bgc-o2_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean dissolved oxygen (3d)
    "cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1D-m_202012",  # noqa: E501 Daily-mean chlorophyll concentration in diatoms (3d)
    "cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1M-m_202012",  # noqa: E501 Monthly-mean chlorophyll concentration in diatoms (3d)
    "cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1D-m_202012",  # noqa: E501 Daily-mean chlorophyll concentration in dinoflagellates (3d)
    "cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1M-m_202012",  # noqa: E501 Monthly-mean chlorophyll concentration in dinoflagellates (3d)
    "cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1D-m_202012",  # noqa: E501 Daily-mean chlorophyll concentration in nanophytoplankton (3d)
    "cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1M-m_202012",  # noqa: E501 Monthly-mean chlorophyll concentration in nanophytoplankton (3d)
    "cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1D-m_202012",  # noqa: E501 Daily-mean chlorophyll concentration in picophytoplankton (3d)
    "cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1M-m_202012",  # noqa: E501 Monthly-mean chlorophyll concentration in picophytoplankton (3d)
    "cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m_202105",  # noqa: E501 Monthly-mean chlorophyll concentration in diatoms (3d)
    "cmems_mod_nws_bgc-pft_myint_7km-3D-dino_P1M-m_202105",  # noqa: E501 Monthly-mean chlorophyll concentration in dinoflagellates (3d)
    "cmems_mod_nws_bgc-pft_myint_7km-3D-nano_P1M-m_202105",  # noqa: E501 Monthly-mean chlorophyll concentration in nanophytoplankton (3d)
    "cmems_mod_nws_bgc-pft_myint_7km-3D-pico_P1M-m_202105",  # noqa: E501 Monthly-mean chlorophyll concentration in picophytoplankton (3d)
    "cmems_mod_nws_bgc-ph_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean ph (3d)
    "cmems_mod_nws_bgc-ph_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean ph (3d)
    "cmems_mod_nws_bgc-ph_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean ph (3d)
    "cmems_mod_nws_bgc-phyc_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean phytoplankton (3d)
    "cmems_mod_nws_bgc-phyc_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean phytoplankton (3d)
    "cmems_mod_nws_bgc-phyc_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean phytoplankton (3d)
    "cmems_mod_nws_bgc-po4_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean phosphate (3d)
    "cmems_mod_nws_bgc-po4_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean phosphate (3d)
    "cmems_mod_nws_bgc-po4_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean phosphate (3d)
    "cmems_mod_nws_bgc-pp_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean net primary production (3d)
    "cmems_mod_nws_bgc-pp_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean net primary production (3d)
    "cmems_mod_nws_bgc-pp_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean net primary production (3d)
    "cmems_mod_nws_bgc-spco2_my_7km-2D_P1D-m_202012",  # noqa: E501 Daily-mean spco2 (2d)
    "cmems_mod_nws_bgc-spco2_my_7km-2D_P1M-m_202012",  # noqa: E501 Monthly-mean spco2 (2d)
    "cmems_mod_nws_bgc-spco2_myint_7km-2D_P1M-m_202105",  # noqa: E501 Monthly-mean spco2 (2d)
]


class nwshelf_multiyear_bgc(Main):
    name = "EO:MO:DAT:NWSHELF_MULTIYEAR_BGC_004_011"
    dataset = "EO:MO:DAT:NWSHELF_MULTIYEAR_BGC_004_011"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
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
        if layer == "cmems_mod_nws_bgc-chl_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-chl_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-chl_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-kd_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-kd_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-kd_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-no3_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-no3_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-no3_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-o2_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-o2_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-o2_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-diato_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-dino_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-nano_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_my_7km-3D-pico_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_myint_7km-3D-dino_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_myint_7km-3D-nano_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pft_myint_7km-3D-pico_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-ph_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-ph_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-ph_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-phyc_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-phyc_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-phyc_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-po4_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-po4_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-po4_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pp_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pp_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pp_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-spco2_my_7km-2D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-spco2_my_7km-2D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-spco2_myint_7km-2D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
