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
    "cmems_mod_nws_phy-bottomt_my_7km-2D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_phy-bottomt_my_7km-2D_P1D-m
    "cmems_mod_nws_phy-bottomt_my_7km-2D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_phy-bottomt_my_7km-2D_P1M-m
    "cmems_mod_nws_phy-bottomt_my_7km-2D_PT1H-i_202112",  # noqa: E501 cmems_mod_nws_phy-bottomt_my_7km-2D_PT1H-i
    "cmems_mod_nws_phy-bottomt_myint_7km-2D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_phy-bottomt_myint_7km-2D_P1M-m
    "cmems_mod_nws_phy-mld_my_7km-2D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_phy-mld_my_7km-2D_P1D-m
    "cmems_mod_nws_phy-mld_my_7km-2D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_phy-mld_my_7km-2D_P1M-m
    "cmems_mod_nws_phy-mld_my_7km-2D_PT1H-i_202112",  # noqa: E501 cmems_mod_nws_phy-mld_my_7km-2D_PT1H-i
    "cmems_mod_nws_phy-mld_myint_7km-2D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_phy-mld_myint_7km-2D_P1M-m
    "cmems_mod_nws_phy-s_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_phy-s_my_7km-3D_P1D-m
    "cmems_mod_nws_phy-s_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_phy-s_my_7km-3D_P1M-m
    "cmems_mod_nws_phy-s_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_phy-s_myint_7km-3D_P1M-m
    "cmems_mod_nws_phy-ssh_my_7km-2D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_phy-ssh_my_7km-2D_P1D-m
    "cmems_mod_nws_phy-ssh_my_7km-2D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_phy-ssh_my_7km-2D_P1M-m
    "cmems_mod_nws_phy-ssh_my_7km-2D_PT1H-i_202112",  # noqa: E501 cmems_mod_nws_phy-ssh_my_7km-2D_PT1H-i
    "cmems_mod_nws_phy-ssh_myint_7km-2D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_phy-ssh_myint_7km-2D_P1M-m
    "cmems_mod_nws_phy-sss_my_7km-2D_PT1H-i_202112",  # noqa: E501 cmems_mod_nws_phy-sss_my_7km-2D_PT1H-i
    "cmems_mod_nws_phy-sst_my_7km-2D_PT1H-i_202112",  # noqa: E501 cmems_mod_nws_phy-sst_my_7km-2D_PT1H-i
    "cmems_mod_nws_phy-t_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_phy-t_my_7km-3D_P1D-m
    "cmems_mod_nws_phy-t_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_phy-t_my_7km-3D_P1M-m
    "cmems_mod_nws_phy-t_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_phy-t_myint_7km-3D_P1M-m
    "cmems_mod_nws_phy-uv_my_7km-2D_PT1H-i_202112",  # noqa: E501 cmems_mod_nws_phy-uv_my_7km-2D_PT1H-i
    "cmems_mod_nws_phy-uv_my_7km-3D_P1D-m_202012",  # noqa: E501 cmems_mod_nws_phy-uv_my_7km-3D_P1D-m
    "cmems_mod_nws_phy-uv_my_7km-3D_P1M-m_202012",  # noqa: E501 cmems_mod_nws_phy-uv_my_7km-3D_P1M-m
    "cmems_mod_nws_phy-uv_myint_7km-3D_P1M-m_202105",  # noqa: E501 cmems_mod_nws_phy-uv_myint_7km-3D_P1M-m
]


class nwshelf_multiyear_phy(Main):
    name = "EO:MO:DAT:NWSHELF_MULTIYEAR_PHY_004_009"
    dataset = "EO:MO:DAT:NWSHELF_MULTIYEAR_PHY_004_009"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "latitude",
            "longitude",
            "mlotst",
            "so",
            "thetao",
            "time",
            "uo",
            "vo",
            "zos",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="9991-12-28T00:00:00Z",
        min_date="1-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_nws_phy-bottomt_my_7km-2D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-bottomt_my_7km-2D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-bottomt_my_7km-2D_PT1H-i_202112":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-bottomt_myint_7km-2D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-mld_my_7km-2D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-mld_my_7km-2D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-mld_my_7km-2D_PT1H-i_202112":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-mld_myint_7km-2D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-s_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-s_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-s_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-ssh_my_7km-2D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-ssh_my_7km-2D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-ssh_my_7km-2D_PT1H-i_202112":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-ssh_myint_7km-2D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-sss_my_7km-2D_PT1H-i_202112":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-sst_my_7km-2D_PT1H-i_202112":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-t_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-t_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-t_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-uv_my_7km-2D_PT1H-i_202112":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-uv_my_7km-3D_P1D-m_202012":
            if min_date is None:
                min_date = "1-01-01T00:00:00Z"

            if max_date is None:
                max_date = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-uv_my_7km-3D_P1M-m_202012":
            if min_date is None:
                min_date = "1993-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2023-08-16T12:00:00Z"

        if layer == "cmems_mod_nws_phy-uv_myint_7km-3D_P1M-m_202105":
            if min_date is None:
                min_date = "2021-05-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-16T12:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
