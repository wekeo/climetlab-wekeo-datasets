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
    "cmems_mod_blk_phy-cur_anfc_2.5km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-cur_anfc_2.5km_P1D-m
    "cmems_mod_blk_phy-cur_anfc_2.5km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_phy-cur_anfc_2.5km_P1M-m
    "cmems_mod_blk_phy-cur_anfc_2.5km_PT15M-i_202311",  # noqa: E501 cmems_mod_blk_phy-cur_anfc_2.5km_PT15M-i
    "cmems_mod_blk_phy-cur_anfc_2.5km_PT1H-m_202311",  # noqa: E501 cmems_mod_blk_phy-cur_anfc_2.5km_PT1H-m
    "cmems_mod_blk_phy-cur_anfc_detided_2.5km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-cur_anfc_detided_2.5km_P1D-m
    "cmems_mod_blk_phy-cur_anfc_mrm-500m_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-cur_anfc_mrm-500m_P1D-m
    "cmems_mod_blk_phy-cur_anfc_mrm-500m_PT1H-i_202311",  # noqa: E501 cmems_mod_blk_phy-cur_anfc_mrm-500m_PT1H-i
    "cmems_mod_blk_phy-mld_anfc_2.5km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-mld_anfc_2.5km_P1D-m
    "cmems_mod_blk_phy-mld_anfc_2.5km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_phy-mld_anfc_2.5km_P1M-m
    "cmems_mod_blk_phy-mld_anfc_2.5km_PT1H-m_202311",  # noqa: E501 cmems_mod_blk_phy-mld_anfc_2.5km_PT1H-m
    "cmems_mod_blk_phy-sal_anfc_2.5km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-sal_anfc_2.5km_P1D-m
    "cmems_mod_blk_phy-sal_anfc_2.5km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_phy-sal_anfc_2.5km_P1M-m
    "cmems_mod_blk_phy-sal_anfc_2.5km_PT1H-m_202311",  # noqa: E501 cmems_mod_blk_phy-sal_anfc_2.5km_PT1H-m
    "cmems_mod_blk_phy-sal_anfc_mrm-500m_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-sal_anfc_mrm-500m_P1D-m
    "cmems_mod_blk_phy-sal_anfc_mrm-500m_PT1H-i_202311",  # noqa: E501 cmems_mod_blk_phy-sal_anfc_mrm-500m_PT1H-i
    "cmems_mod_blk_phy-ssh_anfc_2.5km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-ssh_anfc_2.5km_P1D-m
    "cmems_mod_blk_phy-ssh_anfc_2.5km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_phy-ssh_anfc_2.5km_P1M-m
    "cmems_mod_blk_phy-ssh_anfc_2.5km_PT15M-i_202311",  # noqa: E501 cmems_mod_blk_phy-ssh_anfc_2.5km_PT15M-i
    "cmems_mod_blk_phy-ssh_anfc_2.5km_PT1H-m_202311",  # noqa: E501 cmems_mod_blk_phy-ssh_anfc_2.5km_PT1H-m
    "cmems_mod_blk_phy-ssh_anfc_detided_2.5km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-ssh_anfc_detided_2.5km_P1D-m
    "cmems_mod_blk_phy-ssh_anfc_mrm-500m_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-ssh_anfc_mrm-500m_P1D-m
    "cmems_mod_blk_phy-ssh_anfc_mrm-500m_PT1H-i_202311",  # noqa: E501 cmems_mod_blk_phy-ssh_anfc_mrm-500m_PT1H-i
    "cmems_mod_blk_phy-tem_anfc_2.5km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-tem_anfc_2.5km_P1D-m
    "cmems_mod_blk_phy-tem_anfc_2.5km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_phy-tem_anfc_2.5km_P1M-m
    "cmems_mod_blk_phy-tem_anfc_2.5km_PT1H-m_202311",  # noqa: E501 cmems_mod_blk_phy-tem_anfc_2.5km_PT1H-m
    "cmems_mod_blk_phy-tem_anfc_mrm-500m_P1D-m_202311",  # noqa: E501 cmems_mod_blk_phy-tem_anfc_mrm-500m_P1D-m
    "cmems_mod_blk_phy-tem_anfc_mrm-500m_PT1H-i_202311",  # noqa: E501 cmems_mod_blk_phy-tem_anfc_mrm-500m_PT1H-i
    "cmems_mod_blk_phy_anfc_2.5km_static_202311",  # noqa: E501 cmems_mod_blk_phy_anfc_2.5km_static
    "cmems_mod_blk_phy_anfc_mrm-500m_static_202311",  # noqa: E501 cmems_mod_blk_phy_anfc_mrm-500m_static
]


class blksea_analysisforecast_phy(Main):
    name = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_PHY_007_001"
    dataset = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_PHY_007_001"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "deptho",
            "lat",
            "latitude",
            "lon",
            "longitude",
            "mask",
            "mdt",
            "mlotst",
            "so",
            "thetao",
            "time",
            "uo",
            "vo",
            "wo",
            "zos",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-04-11T12:00:00Z",
        min_date="2021-12-21T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_blk_phy-cur_anfc_2.5km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_anfc_2.5km_P1M-m_202311":
            if min_date is None:
                min_date = "2022-01-14T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_anfc_2.5km_PT15M-i_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-07T00:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_anfc_2.5km_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-06T23:30:00Z"

        if layer == "cmems_mod_blk_phy-cur_anfc_detided_2.5km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-10T12:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_anfc_mrm-500m_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-10T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-09T12:00:00Z"

        if layer == "cmems_mod_blk_phy-cur_anfc_mrm-500m_PT1H-i_202311":
            if min_date is None:
                min_date = "2022-09-12T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-09T23:30:00Z"

        if layer == "cmems_mod_blk_phy-mld_anfc_2.5km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_phy-mld_anfc_2.5km_P1M-m_202311":
            if min_date is None:
                min_date = "2022-01-14T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_phy-mld_anfc_2.5km_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-06T23:30:00Z"

        if layer == "cmems_mod_blk_phy-sal_anfc_2.5km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_phy-sal_anfc_2.5km_P1M-m_202311":
            if min_date is None:
                min_date = "2022-01-14T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_phy-sal_anfc_2.5km_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-06T23:30:00Z"

        if layer == "cmems_mod_blk_phy-sal_anfc_mrm-500m_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-10T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-09T12:00:00Z"

        if layer == "cmems_mod_blk_phy-sal_anfc_mrm-500m_PT1H-i_202311":
            if min_date is None:
                min_date = "2022-09-12T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-09T23:30:00Z"

        if layer == "cmems_mod_blk_phy-ssh_anfc_2.5km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_anfc_2.5km_P1M-m_202311":
            if min_date is None:
                min_date = "2022-01-14T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_anfc_2.5km_PT15M-i_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-07T00:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_anfc_2.5km_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-06T23:30:00Z"

        if layer == "cmems_mod_blk_phy-ssh_anfc_detided_2.5km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-10T12:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_anfc_mrm-500m_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-10T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-09T12:00:00Z"

        if layer == "cmems_mod_blk_phy-ssh_anfc_mrm-500m_PT1H-i_202311":
            if min_date is None:
                min_date = "2022-09-12T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-09T23:30:00Z"

        if layer == "cmems_mod_blk_phy-tem_anfc_2.5km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_phy-tem_anfc_2.5km_P1M-m_202311":
            if min_date is None:
                min_date = "2022-01-14T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_phy-tem_anfc_2.5km_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-12-21T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-06T23:30:00Z"

        if layer == "cmems_mod_blk_phy-tem_anfc_mrm-500m_P1D-m_202311":
            if min_date is None:
                min_date = "2021-12-10T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-09T12:00:00Z"

        if layer == "cmems_mod_blk_phy-tem_anfc_mrm-500m_PT1H-i_202311":
            if min_date is None:
                min_date = "2022-09-12T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-09T23:30:00Z"

        if layer == "cmems_mod_blk_phy_anfc_2.5km_static_202311":
            if min_date is None:
                min_date = "2023-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-28T00:00:00Z"

        if layer == "cmems_mod_blk_phy_anfc_mrm-500m_static_202311":
            if min_date is None:
                min_date = "2023-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-28T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
