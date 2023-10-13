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
    "cmems_mod_nws_phy-bottomt_anfc_7km-2D_P1D-m_202105",  # noqa: E501 Daily-mean seabed temperature (2d)
    "cmems_mod_nws_phy-mld_anfc_7km-2D_P1D-m_202105",  # noqa: E501 Daily-mean mixed layer depth (2d)
    "cmems_mod_nws_phy-s_anfc_7km-3D_P1D-m_202105",  # noqa: E501 Daily-mean salinity (3d)
    "cmems_mod_nws_phy-ssh_anfc_7km-2D_P1D-m_202105",  # noqa: E501 Daily-mean ssh (2d)
    "cmems_mod_nws_phy-t_anfc_7km-3D_P1D-m_202105",  # noqa: E501 Daily-mean potential temperature (3d)
    "cmems_mod_nws_phy-uv_anfc_7km-3D_P1D-m_202105",  # noqa: E501 Daily-mean horizontal velocity (3d)
]


class nwshelf_analysisforecast_phy_lr(Main):
    name = "EO:MO:DAT:NWSHELF_ANALYSISFORECAST_PHY_LR_004_001"
    dataset = "EO:MO:DAT:NWSHELF_ANALYSISFORECAST_PHY_LR_004_001"

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
        if layer == "cmems_mod_nws_phy-ssh_anfc_7km-2D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-09-30T00:00:00Z"

        if layer == "cmems_mod_nws_phy-mld_anfc_7km-2D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-09-30T00:00:00Z"

        if layer == "cmems_mod_nws_phy-s_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-09-30T00:00:00Z"

        if layer == "cmems_mod_nws_phy-bottomt_anfc_7km-2D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-09-30T00:00:00Z"

        if layer == "cmems_mod_nws_phy-t_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-09-30T00:00:00Z"

        if layer == "cmems_mod_nws_phy-uv_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-09-30T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
