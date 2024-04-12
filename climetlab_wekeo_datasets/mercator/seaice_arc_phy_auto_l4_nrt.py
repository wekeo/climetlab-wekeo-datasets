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

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-04-02T00:00:00Z",
        min_date="2020-12-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-si_arc_phy-icetype_nrt_L4-auto_P1D_202105":
            if min_date is None:
                min_date = "2021-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T00:00:00Z"

        if layer == "cmems_obs-si_arc_phy-siconc_nrt_L4-auto_P1D_202105":
            if min_date is None:
                min_date = "2020-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T00:00:00Z"

        if layer == "cmems_obs-si_arc_phy_nrt_l3_P1D_202211":
            if min_date is None:
                min_date = "2021-03-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T20:24:57Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
