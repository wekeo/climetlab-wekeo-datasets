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
    "cmems_mod_ibi_phy_my_0.083deg-2D_PT1H-m_202012",  # noqa: E501 Cmems ibi reanalysis: hourly physical products
    "cmems_mod_ibi_phy_my_0.083deg-3D-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D-climatology_P1M-m_202211
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m_202012",  # noqa: E501 Cmems ibi reanalysis: daily physical products
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m_202012",  # noqa: E501 Cmems ibi reanalysis: monthly physical products
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m_202211",  # noqa: E501 Cmems ibi reanalysis: yearly physical products
]


class ibi_multiyear_phy(Main):
    name = "EO:MO:DAT:IBI_MULTIYEAR_PHY_005_002"
    dataset = "EO:MO:DAT:IBI_MULTIYEAR_PHY_005_002"

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
            "bottomT_standard_deviation",
            "depth",
            "latitude",
            "longitude",
            "mlotst",
            "mlotst_mean",
            "mlotst_standard_deviation",
            "so",
            "so_mean",
            "so_standard_deviation",
            "thetao",
            "thetao_mean",
            "thetao_standard_deviation",
            "time",
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
        if layer == "cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_phy_my_0.083deg-2D_PT1H-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_phy_my_0.083deg-3D-climatology_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-28T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
