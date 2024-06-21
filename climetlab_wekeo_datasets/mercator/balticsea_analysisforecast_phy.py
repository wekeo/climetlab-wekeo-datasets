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
    "cmems_mod_bal_phy-cur_anfc_detided_P1D-m_202311",  # noqa: E501 cmems_mod_bal_phy-cur_anfc_detided_P1D-m
    "cmems_mod_bal_phy-ssh_anfc_detided_P1D-m_202311",  # noqa: E501 cmems_mod_bal_phy-ssh_anfc_detided_P1D-m
    "cmems_mod_bal_phy_anfc_P1D-m_202311",  # noqa: E501 cmems_mod_bal_phy_anfc_P1D-m
    "cmems_mod_bal_phy_anfc_P1M-m_202311",  # noqa: E501 cmems_mod_bal_phy_anfc_P1M-m
    "cmems_mod_bal_phy_anfc_PT15M-i_202311",  # noqa: E501 cmems_mod_bal_phy_anfc_PT15M-i
    "cmems_mod_bal_phy_anfc_PT1H-i_202311",  # noqa: E501 cmems_mod_bal_phy_anfc_PT1H-i
]


class balticsea_analysisforecast_phy(Main):
    name = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_PHY_003_006"
    dataset = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_PHY_003_006"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "bottomT",
            "mlotst",
            "siconc",
            "sithick",
            "sla",
            "so",
            "sob",
            "thetao",
            "uo",
            "uos_detided",
            "vo",
            "vos_detided",
            "wo",
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
        end_datetime="2024-06-26T00:00:00Z",
        start_datetime="2021-11-01T00:15:00Z",
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
