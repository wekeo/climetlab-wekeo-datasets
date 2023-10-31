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
    "cmems_mod_nws_phy-bottomt_my_7km-2D_P1D-m_202012",  # noqa: E501 Daily-mean seabed temperature (2d)
    "cmems_mod_nws_phy-bottomt_my_7km-2D_P1M-m_202012",  # noqa: E501 Monthly-mean seabed temperature (2d)
    "cmems_mod_nws_phy-bottomt_my_7km-2D_PT1H-i_202112",  # noqa: E501 Hourly-instantaneous seabed temperature (2d)
    "cmems_mod_nws_phy-bottomt_myint_7km-2D_P1M-m_202105",  # noqa: E501 Monthly-mean seabed temperature (2d)
    "cmems_mod_nws_phy-mld_my_7km-2D_P1D-m_202012",  # noqa: E501 Daily-mean mixed layer depth (2d)
    "cmems_mod_nws_phy-mld_my_7km-2D_P1M-m_202012",  # noqa: E501 Monthly-mean mixed layer depth (2d)
    "cmems_mod_nws_phy-mld_my_7km-2D_PT1H-i_202112",  # noqa: E501 Hourly-instantaneous mixed layer depth (2d)
    "cmems_mod_nws_phy-mld_myint_7km-2D_P1M-m_202105",  # noqa: E501 Monthly-mean mixed layer depth (2d)
    "cmems_mod_nws_phy-s_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean salinity (3d)
    "cmems_mod_nws_phy-s_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean salinity (3d)
    "cmems_mod_nws_phy-s_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean salinity (3d)
    "cmems_mod_nws_phy-ssh_my_7km-2D_P1D-m_202012",  # noqa: E501 Daily-mean ssh (2d)
    "cmems_mod_nws_phy-ssh_my_7km-2D_P1M-m_202012",  # noqa: E501 Monthly-mean ssh (2d)
    "cmems_mod_nws_phy-ssh_my_7km-2D_PT1H-i_202112",  # noqa: E501 Hourly-instantaneous ssh (2d)
    "cmems_mod_nws_phy-ssh_myint_7km-2D_P1M-m_202105",  # noqa: E501 Monthly-mean ssh (2d)
    "cmems_mod_nws_phy-sss_my_7km-2D_PT1H-i_202112",  # noqa: E501 Hourly-instantaneous surface salinity (2d)
    "cmems_mod_nws_phy-sst_my_7km-2D_PT1H-i_202112",  # noqa: E501 Hourly-instantaneous surface temperature (2d)
    "cmems_mod_nws_phy-t_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean potential temperature (3d)
    "cmems_mod_nws_phy-t_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean potential temperature (3d)
    "cmems_mod_nws_phy-t_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean potential temperature (3d)
    "cmems_mod_nws_phy-uv_my_7km-2D_PT1H-i_202112",  # noqa: E501 Hourly-instantaneous horizontal velocity (2d)
    "cmems_mod_nws_phy-uv_my_7km-3D_P1D-m_202012",  # noqa: E501 Daily-mean horizontal velocity (3d)
    "cmems_mod_nws_phy-uv_my_7km-3D_P1M-m_202012",  # noqa: E501 Monthly-mean horizontal velocity (3d)
    "cmems_mod_nws_phy-uv_myint_7km-3D_P1M-m_202105",  # noqa: E501 Monthly-mean horizontal velocity (3d)
]


class nwshelf_multiyear_phy(Main):
    name = "EO:MO:DAT:NWSHELF_MULTIYEAR_PHY_004_009"
    dataset = "EO:MO:DAT:NWSHELF_MULTIYEAR_PHY_004_009"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
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
        if layer == "cmems_mod_nws_phy-bottomt_my_7km-2D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-bottomt_my_7km-2D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-bottomt_my_7km-2D_PT1H-i_202112":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-bottomt_myint_7km-2D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-mld_my_7km-2D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-mld_my_7km-2D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-mld_my_7km-2D_PT1H-i_202112":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-mld_myint_7km-2D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-s_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-s_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-s_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-ssh_my_7km-2D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-ssh_my_7km-2D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-ssh_my_7km-2D_PT1H-i_202112":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-ssh_myint_7km-2D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-sss_my_7km-2D_PT1H-i_202112":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-sst_my_7km-2D_PT1H-i_202112":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-t_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-t_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-t_myint_7km-3D_P1M-m_202105":
            if start is None:
                start = "2021-05-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-uv_my_7km-2D_PT1H-i_202112":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-uv_my_7km-3D_P1D-m_202012":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-uv_my_7km-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2022-12-28T00:00:00Z"

        if layer == "cmems_mod_nws_phy-uv_myint_7km-3D_P1M-m_202105":
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
