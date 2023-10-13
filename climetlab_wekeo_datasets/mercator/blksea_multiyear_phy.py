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
    "bs-cmcc-tem-rean-m_202012",  # noqa: E501 bs-cmcc-tem-rean-m_202012
    "cmems_mod_blk_phy-cur_my_2.5km-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-cur_my_2.5km-climatology_P1M-m_202211
    "cmems_mod_blk_phy-cur_my_2.5km_P1D-m_202211",  # noqa: E501 Horizontal velocity (3d) - daily mean
    "cmems_mod_blk_phy-cur_my_2.5km_P1M-m_202211",  # noqa: E501 Horizontal velocity (3d) - monthly mean
    "cmems_mod_blk_phy-cur_my_2.5km_P1Y-m_202211",  # noqa: E501 Horizontal velocity (3d) - yearly mean
    "cmems_mod_blk_phy-cur_myint_2.5km_P1M-m_202211",  # noqa: E501 Horizontal velocity (3d) - monthly mean
    "cmems_mod_blk_phy-mld_my_2.5km-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-mld_my_2.5km-climatology_P1M-m_202211
    "cmems_mod_blk_phy-mld_my_2.5km_P1D-m_202211",  # noqa: E501 Mixed layer depth (2d) - daily mean
    "cmems_mod_blk_phy-mld_my_2.5km_P1M-m_202211",  # noqa: E501 Mixed layer depth (2d) - monthly mean
    "cmems_mod_blk_phy-mld_my_2.5km_P1Y-m_202211",  # noqa: E501 Mixed layer depth (2d) - yearly mean
    "cmems_mod_blk_phy-mld_myint_2.5km_P1M-m_202211",  # noqa: E501 Mixed layer depth (2d) - monthly mean
    "cmems_mod_blk_phy-sal_my_2.5km-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-sal_my_2.5km-climatology_P1M-m_202211
    "cmems_mod_blk_phy-sal_my_2.5km_P1D-m_202211",  # noqa: E501 Salinity (3d) - daily mean
    "cmems_mod_blk_phy-sal_my_2.5km_P1M-m_202211",  # noqa: E501 Salinity (3d) - monthly mean
    "cmems_mod_blk_phy-sal_my_2.5km_P1Y-m_202211",  # noqa: E501 Salinity (3d) - yearly mean
    "cmems_mod_blk_phy-sal_myint_2.5km_P1M-m_202211",  # noqa: E501 Salinity (3d) - monthly mean
    "cmems_mod_blk_phy-ssh_my_2.5km-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-ssh_my_2.5km-climatology_P1M-m_202211
    "cmems_mod_blk_phy-ssh_my_2.5km_P1D-m_202211",  # noqa: E501 Sea surface height (2d) - daily mean
    "cmems_mod_blk_phy-ssh_my_2.5km_P1M-m_202211",  # noqa: E501 Sea surface height (2d) - monthly mean
    "cmems_mod_blk_phy-ssh_my_2.5km_P1Y-m_202211",  # noqa: E501 Sea surface height (2d) - yearly mean
    "cmems_mod_blk_phy-ssh_myint_2.5km_P1M-m_202211",  # noqa: E501 Sea surface height (2d) - monthly mean
    "cmems_mod_blk_phy-tem_my_2.5km-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-tem_my_2.5km-climatology_P1M-m_202211
    "cmems_mod_blk_phy-tem_my_2.5km_P1D-m_202211",  # noqa: E501 Potential temperature (3d), bottom temperature (2d) - daily mean
    "cmems_mod_blk_phy-tem_my_2.5km_P1M-m_202211",  # noqa: E501 Potential temperature (3d), bottom temperature (2d) - monthly mean
    "cmems_mod_blk_phy-tem_my_2.5km_P1Y-m_202211",  # noqa: E501 Potential temperature (3d), bottom temperature (2d) - yearly mean
    "cmems_mod_blk_phy-tem_myint_2.5km_P1M-m_202211",  # noqa: E501 Potential temperature (3d), bottom temperature (2d) - monthly mean
]


class blksea_multiyear_phy(Main):
    name = "EO:MO:DAT:BLKSEA_MULTIYEAR_PHY_007_004"
    dataset = "EO:MO:DAT:BLKSEA_MULTIYEAR_PHY_007_004"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "bottomT",
            "bottomT_mean",
            "bottomT_std",
            "climatology_bounds",
            "depth",
            "lat",
            "lon",
            "mlotst",
            "mlotst_mean",
            "mlotst_std",
            "so",
            "so_mean",
            "so_std",
            "thetao",
            "thetao_mean",
            "thetao_std",
            "time",
            "uo",
            "uo_mean",
            "uo_std",
            "vo",
            "vo_mean",
            "vo_std",
            "zos",
            "zos_mean",
            "zos_std",
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
        if layer == "cmems_mod_blk_phy-mld_my_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-mld_myint_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_my_2.5km-climatology_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-mld_my_2.5km-climatology_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-tem_my_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-sal_my_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-mld_my_2.5km_P1Y-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_my_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-tem_myint_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "cmems_mod_blk_phy-sal_my_2.5km_P1Y-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_myint_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "cmems_mod_blk_phy-mld_my_2.5km_P1D-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_my_2.5km_P1D-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_my_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_myint_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "cmems_mod_blk_phy-tem_my_2.5km_P1D-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_my_2.5km_P1Y-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-tem_my_2.5km_P1Y-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-tem_my_2.5km-climatology_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-sal_myint_2.5km_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "cmems_mod_blk_phy-sal_my_2.5km_P1D-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_my_2.5km_P1Y-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_my_2.5km-climatology_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_my_2.5km_P1D-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_blk_phy-sal_my_2.5km-climatology_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
