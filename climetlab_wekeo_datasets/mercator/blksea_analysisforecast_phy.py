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
]


class blksea_analysisforecast_phy(Main):
    name = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_PHY_007_001"
    dataset = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_PHY_007_001"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "bottomT",
            "mlotst",
            "so",
            "thetao",
            "uo",
            "vo",
            "wo",
            "zos",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-1",
            "-2",
            "-3",
            "-4",
            "-5",
            "-6",
            "-7",
            "-8",
            "-9",
            "-10",
            "-11",
            "-12",
            "-13",
            "-14",
            "-15",
            "-16",
            "-17",
            "-18",
            "-19",
            "-20",
            "-21",
            "-22",
            "-23",
            "-24",
            "-25",
            "-26",
            "-27",
            "-28",
            "-29",
            "-30",
            "-31",
            "-32",
            "-33",
            "-34",
            "-35",
            "-36",
            "-37",
            "-38",
            "-39",
            "-40",
            "-41",
            "-42",
            "-43",
            "-44",
            "-45",
            "-46",
            "-47",
            "-48",
            "-49",
            "-50",
            "-55",
            "-60",
            "-65",
            "-70",
            "-75",
            "-80",
            "-85",
            "-90",
            "-95",
            "-100",
            "-120",
            "-140",
            "-160",
            "-180",
            "-200",
            "-250",
            "-300",
            "-350",
            "-400",
            "-450",
            "-500",
            "-550",
            "-600",
            "-650",
            "-700",
            "-750",
            "-800",
            "-850",
            "-900",
            "-950",
            "-1000",
            "-1100",
            "-1200",
            "-1300",
            "-1400",
            "-1500",
            "-1600",
            "-1700",
            "-1800",
            "-1900",
            "-2000",
            "-2100",
            "-2200",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-1",
            "-2",
            "-3",
            "-4",
            "-5",
            "-6",
            "-7",
            "-8",
            "-9",
            "-10",
            "-11",
            "-12",
            "-13",
            "-14",
            "-15",
            "-16",
            "-17",
            "-18",
            "-19",
            "-20",
            "-21",
            "-22",
            "-23",
            "-24",
            "-25",
            "-26",
            "-27",
            "-28",
            "-29",
            "-30",
            "-31",
            "-32",
            "-33",
            "-34",
            "-35",
            "-36",
            "-37",
            "-38",
            "-39",
            "-40",
            "-41",
            "-42",
            "-43",
            "-44",
            "-45",
            "-46",
            "-47",
            "-48",
            "-49",
            "-50",
            "-55",
            "-60",
            "-65",
            "-70",
            "-75",
            "-80",
            "-85",
            "-90",
            "-95",
            "-100",
            "-120",
            "-140",
            "-160",
            "-180",
            "-200",
            "-250",
            "-300",
            "-350",
            "-400",
            "-450",
            "-500",
            "-550",
            "-600",
            "-650",
            "-700",
            "-750",
            "-800",
            "-850",
            "-900",
            "-950",
            "-1000",
            "-1100",
            "-1200",
            "-1300",
            "-1400",
            "-1500",
            "-1600",
            "-1700",
            "-1800",
            "-1900",
            "-2000",
            "-2100",
            "-2200",
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
        end_datetime="2024-06-26T23:00:00Z",
        start_datetime="2022-09-12T00:00:00Z",
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
