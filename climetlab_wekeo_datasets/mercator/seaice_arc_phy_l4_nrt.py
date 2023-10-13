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
    "esa_obs-si_arc_phy-sit_nrt_l4_multi_P1D-m_202207",  # noqa: E501 Sea ice thickness derived from merging cryosat-2 and smos ice thickness
]


class seaice_arc_phy_l4_nrt(Main):
    name = "EO:MO:DAT:SEAICE_ARC_PHY_L4_NRT_011_014"
    dataset = "EO:MO:DAT:SEAICE_ARC_PHY_L4_NRT_011_014"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "Lambert_Azimuthal_Grid",
            "analysis_sea_ice_thickness",
            "analysis_sea_ice_thickness_unc",
            "background_sea_ice_thickness",
            "correlation_length_scale",
            "cryosat_sea_ice_thickness",
            "cryosat_sea_ice_thickness_uncertainty",
            "innovation",
            "lat",
            "lon",
            "sea_ice_concentration",
            "sea_ice_type",
            "smos_sea_ice_thickness",
            "smos_sea_ice_thickness_uncertainty",
            "time",
            "time_bnds",
            "weighted_mean_sea_ice_thickness",
            "xc",
            "yc",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="esa_obs-si_arc_phy-sit_nrt_l4_multi_P1D-m_202207",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "esa_obs-si_arc_phy-sit_nrt_l4_multi_P1D-m_202207":
            if start is None:
                start = "2019-10-28T00:00:00Z"

            if end is None:
                end = "2023-04-16T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
