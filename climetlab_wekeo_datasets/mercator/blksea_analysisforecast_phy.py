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
    def __init__(self, layer, variables, bbox=None, limit=None):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
