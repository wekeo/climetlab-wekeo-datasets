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
    "cmems_mod_ibi_phy_my_0.083deg-2D_PT1H-m_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-2D_PT1H-m
    "cmems_mod_ibi_phy_my_0.083deg-3D-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D-climatology_P1M-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m_202211",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m
]


class ibi_multiyear_phy(Main):
    name = "EO:MO:DAT:IBI_MULTIYEAR_PHY_005_002"
    dataset = "EO:MO:DAT:IBI_MULTIYEAR_PHY_005_002"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "bottomT",
            "bottomT_mean",
            "bottomT_standard_deviation",
            "mlotst",
            "mlotst_mean",
            "mlotst_standard_deviation",
            "so",
            "so_mean",
            "so_standard_deviation",
            "thetao",
            "thetao_mean",
            "thetao_standard_deviation",
            "ubar",
            "uo",
            "uo_mean",
            "uo_standard_deviation",
            "vbar",
            "vo",
            "vo_mean",
            "vo_standard_deviation",
            "zos",
            "zos_mean",
            "zos_standard_deviation",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        end_datetime="2021-12-28T23:00:00Z",
        start_datetime="1993-01-01T00:00:00Z",
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
