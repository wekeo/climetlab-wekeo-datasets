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
    "cmems_mod_ibi_phy_my_0.083deg-2D_PT1H-m_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-2D_PT1H-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m_202012",  # noqa: E501 Cmems ibi reanalysis: daily physical products
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m_202012",  # noqa: E501 Cmems ibi reanalysis: monthly physical products
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m_202211",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m_202211",  # noqa: E501 Cmems ibi reanalysis: yearly physical products
    "cmems_mod_ibi_phy_my_0.083deg-3D_static_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_static
]


class ibi_multiyear_phy(Main):
    name = "EO:MO:DAT:IBI_MULTIYEAR_PHY_005_002"
    dataset = "EO:MO:DAT:IBI_MULTIYEAR_PHY_005_002"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "latitude",
            "longitude",
            "mdt",
            "mlotst",
            "so",
            "thetao",
            "time",
            "ubar",
            "uo",
            "vbar",
            "vo",
            "zos",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2023-01-01T00:00:00Z",
        min_date="2020-12-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_ibi_phy_my_0.083deg-2D_PT1H-m_202012":
            if min_date is None:
                min_date = "2020-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m_202012":
            if min_date is None:
                min_date = "2020-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m_202012":
            if min_date is None:
                min_date = "2020-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m_202211":
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_phy_my_0.083deg-3D_static_202012":
            if min_date is None:
                min_date = "2020-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2020-12-28T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
