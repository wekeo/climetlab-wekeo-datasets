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
    "cmems_mod_med_phy-cur_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-cur_anfc_4.2km-3D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km-3D_PT1H-m
    "cmems_mod_med_phy-cur_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-cur_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i
    "cmems_mod_med_phy-cur_anfc_detided_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_detided_4.2km_P1D-m
    "cmems_mod_med_phy-mld_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-mld_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-mld_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-mld_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-mld_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-mld_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-sal_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-sal_anfc_4.2km-3D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km-3D_PT1H-m
    "cmems_mod_med_phy-sal_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-sal_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-ssh_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i
    "cmems_mod_med_phy-ssh_anfc_detided_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_detided_4.2km_P1D-m
    "cmems_mod_med_phy-tem_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-tem_anfc_4.2km-3D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km-3D_PT1H-m
    "cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-tem_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m
]


class medsea_analysisforecast_phy(Main):
    name = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_PHY_006_013"
    dataset = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_PHY_006_013"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "bottomT",
            "mlotst",
            "so",
            "thetao",
            "uo",
            "uo_detided",
            "vo",
            "vo_detided",
            "wo",
            "zos",
            "zos_detided",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        end_datetime="2024-06-24T23:45:00Z",
        start_datetime="2021-11-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
