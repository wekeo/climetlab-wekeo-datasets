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
    "cmems_mod_bal_phy_my_P1D-m_202303",  # noqa: E501 Cmems nemo daily integrated model fields
    "cmems_mod_bal_phy_my_P1D-m_202303",  # noqa: E501 cmems_mod_bal_phy_my_P1D-m
    "cmems_mod_bal_phy_my_P1M-m_202303",  # noqa: E501 Cmems nemo monthly integrated model fields
    "cmems_mod_bal_phy_my_P1M-m_202303",  # noqa: E501 cmems_mod_bal_phy_my_P1M-m
    "cmems_mod_bal_phy_my_P1Y-m_202303",  # noqa: E501 cmems_mod_bal_phy_my_P1Y-m
    "cmems_mod_bal_phy_my_P1Y-m_202303",  # noqa: E501 Cmems nemo annual integrated model fields
    "cmems_mod_bal_phy_my_static_202303",  # noqa: E501 cmems_mod_bal_phy_my_static
]


class balticsea_multiyear_phy(Main):
    name = "EO:MO:DAT:BALTICSEA_MULTIYEAR_PHY_003_011"
    dataset = "EO:MO:DAT:BALTICSEA_MULTIYEAR_PHY_003_011"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "deptho",
            "deptho_lev",
            "lat",
            "latitude",
            "lon",
            "longitude",
            "mask",
            "mlotst",
            "siconc",
            "sithick",
            "sla",
            "so",
            "sob",
            "thetao",
            "time",
            "uo",
            "vo",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2021-12-31T12:00:00Z",
        min_date="1993-01-01T12:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_bal_phy_my_P1D-m_202303":
            if min_date is None:
                min_date = "1993-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2021-12-31T12:00:00Z"

        if layer == "cmems_mod_bal_phy_my_P1M-m_202303":
            if min_date is None:
                min_date = "1993-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2021-12-01T12:00:00Z"

        if layer == "cmems_mod_bal_phy_my_P1Y-m_202303":
            if min_date is None:
                min_date = "1993-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2021-01-01T12:00:00Z"

        if layer == "cmems_mod_bal_phy_my_static_202303":
            if min_date is None:
                min_date = "2023-03-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-03-28T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
