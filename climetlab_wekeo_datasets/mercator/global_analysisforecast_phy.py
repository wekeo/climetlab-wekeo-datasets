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
    "cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m_202211",  # noqa: E501 Daily mean fields from global ocean physics analysis and forecast updated daily
    "cmems_mod_glo_phy-cur_anfc_0.083deg_P1M-m_202211",  # noqa: E501 Monthly mean fields for product global analysisforecast phy 001 024
    "cmems_mod_glo_phy-cur_anfc_0.083deg_PT6H-i_202211",  # noqa: E501 Instantaneous fields for product global analysisforecast phy 001 024
    "cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m_202211",  # noqa: E501 Daily mean fields from global ocean physics analysis and forecast updated daily
    "cmems_mod_glo_phy-so_anfc_0.083deg_P1M-m_202211",  # noqa: E501 Monthly mean fields for product global analysisforecast phy 001 024
    "cmems_mod_glo_phy-so_anfc_0.083deg_PT6H-i_202211",  # noqa: E501 Instantaneous fields for product global analysisforecast phy 001 024
    "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m_202211",  # noqa: E501 Daily mean fields from global ocean physics analysis and forecast updated daily
    "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1M-m_202211",  # noqa: E501 Monthly mean fields for product global analysisforecast phy 001 024
    "cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i_202211",  # noqa: E501 Instantaneous fields for product global analysisforecast phy 001 024
    "cmems_mod_glo_phy-wcur_anfc_0.083deg_P1D-m_202211",  # noqa: E501 Daily mean fields from global ocean physics analysis and forecast updated daily
    "cmems_mod_glo_phy-wcur_anfc_0.083deg_P1M-m_202211",  # noqa: E501 Monthly mean fields for product global analysisforecast phy 001 024
    "cmems_mod_glo_phy_anfc_0.083deg_P1D-m_202211",  # noqa: E501 Daily mean fields from global ocean physics analysis and forecast updated daily
    "cmems_mod_glo_phy_anfc_0.083deg_P1M-m_202211",  # noqa: E501 Monthly mean fields for product global analysisforecast phy 001 024
    "cmems_mod_glo_phy_anfc_0.083deg_PT1H-m_202211",  # noqa: E501 Hourly mean fields from global ocean physics analysis and forecast updated daily
    "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i_202211",  # noqa: E501 Hourly mean merged surface currents from oceanic circulation, tides and waves
]


class global_analysisforecast_phy(Main):
    name = "EO:MO:DAT:GLOBAL_ANALYSISFORECAST_PHY_001_024"
    dataset = "EO:MO:DAT:GLOBAL_ANALYSISFORECAST_PHY_001_024"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "depth",
            "ist",
            "latitude",
            "longitude",
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
        if layer == "cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-cur_anfc_0.083deg_P1M-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-cur_anfc_0.083deg_PT6H-i_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-so_anfc_0.083deg_P1M-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-so_anfc_0.083deg_PT6H-i_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1M-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-wcur_anfc_0.083deg_P1D-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy-wcur_anfc_0.083deg_P1M-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy_anfc_0.083deg_P1D-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy_anfc_0.083deg_P1M-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy_anfc_0.083deg_PT1H-m_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-30T00:00:00Z"

        if layer == "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i_202211":
            if start is None:
                start = "2020-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
