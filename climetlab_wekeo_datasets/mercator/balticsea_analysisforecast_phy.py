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
    "cmems_mod_bal_phy_anfc_P1D-m_202211",  # noqa: E501 Cmems nemo daily integrated model fields
    "cmems_mod_bal_phy_anfc_P1M-m_202211",  # noqa: E501 Cmems nemo monthly integrated model fields
    "cmems_mod_bal_phy_anfc_PT15m-i_202211",  # noqa: E501 Cmems nemo 15 minutes surface model fields
    "cmems_mod_bal_phy_anfc_PT1h-i_202211",  # noqa: E501 Cmems nemo hourly model fields
]


class balticsea_analysisforecast_phy(Main):
    name = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_PHY_003_006"
    dataset = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_PHY_003_006"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "lat",
            "lon",
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
            "wo",
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
        if layer == "cmems_mod_bal_phy_anfc_P1D-m_202211":
            if start is None:
                start = "2021-01-01T12:00:00Z"

            if end is None:
                end = "2023-11-01T12:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_P1M-m_202211":
            if start is None:
                start = "2021-01-16T12:00:00Z"

            if end is None:
                end = "2023-09-16T06:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_PT15m-i_202211":
            if start is None:
                start = "2021-01-01T00:15:00Z"

            if end is None:
                end = "2023-11-02T12:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_PT1h-i_202211":
            if start is None:
                start = "2021-01-01T01:00:00Z"

            if end is None:
                end = "2023-11-02T12:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
