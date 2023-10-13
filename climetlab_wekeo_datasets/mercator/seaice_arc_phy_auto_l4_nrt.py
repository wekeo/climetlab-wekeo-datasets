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
    "cmems_obs-si_arc_phy-icetype_nrt_L4-auto_P1D_202105",  # noqa: E501 High resolution sea ice type
    "cmems_obs-si_arc_phy-siconc_nrt_L4-auto_P1D_202105",  # noqa: E501 High resolution sea ice concentration
    "cmems_obs-si_arc_phy_nrt_l3_P1D_202211",  # noqa: E501 Dmi-asip sea ice classification
]


class seaice_arc_phy_auto_l4_nrt(Main):
    name = "EO:MO:DAT:SEAICE_ARC_PHY_AUTO_L4_NRT_011_015"
    dataset = "EO:MO:DAT:SEAICE_ARC_PHY_AUTO_L4_NRT_011_015"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "acq_time",
            "conc",
            "confidence",
            "crs",
            "ice_concentration",
            "ice_type",
            "lat",
            "lon",
            "status_flag",
            "time",
            "x",
            "xc",
            "y",
            "yc",
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
        if layer == "cmems_obs-si_arc_phy-icetype_nrt_L4-auto_P1D_202105":
            if start is None:
                start = "2021-01-01T01:00:00Z"

            if end is None:
                end = "2023-09-25T12:00:00Z"

        if layer == "cmems_obs-si_arc_phy-siconc_nrt_L4-auto_P1D_202105":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2023-09-25T12:00:00Z"

        if layer == "cmems_obs-si_arc_phy_nrt_l3_P1D_202211":
            if start is None:
                start = "2021-03-01T07:01:33Z"

            if end is None:
                end = "2023-09-24T19:57:53Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
