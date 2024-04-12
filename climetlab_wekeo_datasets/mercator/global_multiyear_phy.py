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
    "cmems_mod_glo_phy_my_0.083deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_phy_my_0.083deg_P1D-m
    "cmems_mod_glo_phy_my_0.083deg_P1M-m_202311",  # noqa: E501 cmems_mod_glo_phy_my_0.083deg_P1M-m
    "cmems_mod_glo_phy_my_0.083deg_static_202311",  # noqa: E501 cmems_mod_glo_phy_my_0.083deg_static
    "cmems_mod_glo_phy_myint_0.083deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_phy_myint_0.083deg_P1D-m
    "cmems_mod_glo_phy_myint_0.083deg_P1M-m_202311",  # noqa: E501 cmems_mod_glo_phy_myint_0.083deg_P1M-m
]


class global_multiyear_phy(Main):
    name = "EO:MO:DAT:GLOBAL_MULTIYEAR_PHY_001_030"
    dataset = "EO:MO:DAT:GLOBAL_MULTIYEAR_PHY_001_030"

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
            "siconc",
            "sithick",
            "so",
            "thetao",
            "time",
            "uo",
            "usi",
            "vo",
            "vsi",
            "zos",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2023-11-16T00:00:00Z",
        min_date="2021-07-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_glo_phy_my_0.083deg_P1D-m_202311":
            if min_date is None:
                min_date = "1993-01-06T00:00:00Z"

            if max_date is None:
                max_date = "2021-07-07T00:00:00Z"

        if layer == "cmems_mod_glo_phy_my_0.083deg_P1M-m_202311":
            if min_date is None:
                min_date = "1993-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2021-06-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy_my_0.083deg_static_202311":
            if min_date is None:
                min_date = "2023-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-28T00:00:00Z"

        if layer == "cmems_mod_glo_phy_myint_0.083deg_P1D-m_202311":
            if min_date is None:
                min_date = "2021-07-01T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-26T12:00:00Z"

        if layer == "cmems_mod_glo_phy_myint_0.083deg_P1M-m_202311":
            if min_date is None:
                min_date = "2021-07-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-16T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
