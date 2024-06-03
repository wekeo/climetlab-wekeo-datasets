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
    "cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m_202211",  # noqa: E501 cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m
    "cmems_mod_glo_phy-cur_anfc_0.083deg_P1M-m_202211",  # noqa: E501 cmems_mod_glo_phy-cur_anfc_0.083deg_P1M-m
    "cmems_mod_glo_phy-cur_anfc_0.083deg_PT6H-i_202211",  # noqa: E501 cmems_mod_glo_phy-cur_anfc_0.083deg_PT6H-i
    "cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m_202211",  # noqa: E501 cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m
    "cmems_mod_glo_phy-so_anfc_0.083deg_P1M-m_202211",  # noqa: E501 cmems_mod_glo_phy-so_anfc_0.083deg_P1M-m
    "cmems_mod_glo_phy-so_anfc_0.083deg_PT6H-i_202211",  # noqa: E501 cmems_mod_glo_phy-so_anfc_0.083deg_PT6H-i
    "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m_202211",  # noqa: E501 cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m
    "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1M-m_202211",  # noqa: E501 cmems_mod_glo_phy-thetao_anfc_0.083deg_P1M-m
    "cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i_202211",  # noqa: E501 cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i
    "cmems_mod_glo_phy-wcur_anfc_0.083deg_P1D-m_202211",  # noqa: E501 cmems_mod_glo_phy-wcur_anfc_0.083deg_P1D-m
    "cmems_mod_glo_phy-wcur_anfc_0.083deg_P1M-m_202211",  # noqa: E501 cmems_mod_glo_phy-wcur_anfc_0.083deg_P1M-m
    "cmems_mod_glo_phy_anfc_0.083deg_P1D-m_202211",  # noqa: E501 cmems_mod_glo_phy_anfc_0.083deg_P1D-m
    "cmems_mod_glo_phy_anfc_0.083deg_P1M-m_202211",  # noqa: E501 cmems_mod_glo_phy_anfc_0.083deg_P1M-m
    "cmems_mod_glo_phy_anfc_0.083deg_PT1H-m_202211",  # noqa: E501 cmems_mod_glo_phy_anfc_0.083deg_PT1H-m
    "cmems_mod_glo_phy_anfc_0.083deg_static_202211",  # noqa: E501 cmems_mod_glo_phy_anfc_0.083deg_static
    "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i_202211",  # noqa: E501 cmems_mod_glo_phy_anfc_merged-uv_PT1H-i
]


class global_analysisforecast_phy(Main):
    name = "EO:MO:DAT:GLOBAL_ANALYSISFORECAST_PHY_001_024"
    dataset = "EO:MO:DAT:GLOBAL_ANALYSISFORECAST_PHY_001_024"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "depth",
            "deptho",
            "deptho_lev",
            "ist",
            "latitude",
            "longitude",
            "mask",
            "mlotst",
            "pbo",
            "siage",
            "sialb",
            "siconc",
            "sisnthick",
            "sithick",
            "sivelo",
            "so",
            "sob",
            "thetao",
            "time",
            "tob",
            "uo",
            "usi",
            "utide",
            "utotal",
            "vo",
            "vsdx",
            "vsdy",
            "vsi",
            "vtide",
            "vtotal",
            "wo",
            "zos",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-05-22T00:00:00Z",
        min_date="2020-11-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_glo_phy-cur_anfc_0.083deg_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_glo_phy-cur_anfc_0.083deg_PT6H-i_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-21T00:00:00Z"

        if layer == "cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_glo_phy-so_anfc_0.083deg_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_glo_phy-so_anfc_0.083deg_PT6H-i_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-22T00:00:00Z"

        if layer == "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T12:00:00Z"

        if layer == "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-22T00:00:00Z"

        if layer == "cmems_mod_glo_phy-wcur_anfc_0.083deg_P1D-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T12:00:00Z"

        if layer == "cmems_mod_glo_phy-wcur_anfc_0.083deg_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_glo_phy_anfc_0.083deg_P1D-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T12:00:00Z"

        if layer == "cmems_mod_glo_phy_anfc_0.083deg_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_glo_phy_anfc_0.083deg_PT1H-m_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T23:30:00Z"

        if layer == "cmems_mod_glo_phy_anfc_0.083deg_static_202211":
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i_202211":
            if min_date is None:
                min_date = "2020-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T23:30:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
