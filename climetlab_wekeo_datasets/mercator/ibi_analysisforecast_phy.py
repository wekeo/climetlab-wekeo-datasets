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
    "cmems_mod_ibi_phy_anfc_0.027deg-2D_PT15M-i_202211",  # noqa: E501 cmems_mod_ibi_phy_anfc_0.027deg-2D_PT15M-i
    "cmems_mod_ibi_phy_anfc_0.027deg-2D_PT1H-m_202211",  # noqa: E501 cmems_mod_ibi_phy_anfc_0.027deg-2D_PT1H-m
    "cmems_mod_ibi_phy_anfc_0.027deg-3D_P1D-m_202211",  # noqa: E501 cmems_mod_ibi_phy_anfc_0.027deg-3D_P1D-m
    "cmems_mod_ibi_phy_anfc_0.027deg-3D_P1M-m_202211",  # noqa: E501 cmems_mod_ibi_phy_anfc_0.027deg-3D_P1M-m
    "cmems_mod_ibi_phy_anfc_0.027deg-3D_PT1H-m_202211",  # noqa: E501 cmems_mod_ibi_phy_anfc_0.027deg-3D_PT1H-m
    "cmems_mod_ibi_phy_anfc_0.027deg-3D_static_202211",  # noqa: E501 cmems_mod_ibi_phy_anfc_0.027deg-3D_static
]


class ibi_analysisforecast_phy(Main):
    name = "EO:MO:DAT:IBI_ANALYSISFORECAST_PHY_005_001"
    dataset = "EO:MO:DAT:IBI_ANALYSISFORECAST_PHY_005_001"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "e1t",
            "e2t",
            "e3t",
            "latitude",
            "longitude",
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
        bbox,
        layer,
        max_date="2022-11-28T00:00:00Z",
        min_date="2022-11-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_ibi_phy_anfc_0.027deg-2D_PT15M-i_202211":
            if min_date is None:
                min_date = "2021-12-29T00:15:00Z"

            if max_date is None:
                max_date = "2024-05-25T00:00:00Z"

        if layer == "cmems_mod_ibi_phy_anfc_0.027deg-2D_PT1H-m_202211":
            if min_date is None:
                min_date = "2020-11-21T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-24T23:30:00Z"

        if layer == "cmems_mod_ibi_phy_anfc_0.027deg-3D_P1D-m_202211":
            if min_date is None:
                min_date = "2020-11-21T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-24T12:00:00Z"

        if layer == "cmems_mod_ibi_phy_anfc_0.027deg-3D_P1M-m_202211":
            if min_date is None:
                min_date = "2020-12-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T12:00:00Z"

        if layer == "cmems_mod_ibi_phy_anfc_0.027deg-3D_PT1H-m_202211":
            if min_date is None:
                min_date = "2023-12-04T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-24T23:30:00Z"

        if layer == "cmems_mod_ibi_phy_anfc_0.027deg-3D_static_202211":
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-28T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
