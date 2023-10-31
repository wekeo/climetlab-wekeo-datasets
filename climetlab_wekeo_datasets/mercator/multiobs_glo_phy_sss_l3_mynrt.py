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
    "cmems_obs-mob_glo_phy-sss_mynrt_smos_P1D_202211",  # noqa: E501 cmems_obs-mob_glo_phy-sss_mynrt_smos_P1D_202211
]


class multiobs_glo_phy_sss_l3_mynrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_SSS_L3_MYNRT_015_014"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_SSS_L3_MYNRT_015_014"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "Mean_Acq_Time",
            "Sea_Surface_Salinity",
            "Sea_Surface_Salinity_Error",
            "Sea_Surface_Salinity_QC",
            "Sea_Surface_Salinity_Rain_Corrected",
            "Sea_Surface_Salinity_Rain_Corrected_Error",
            "X_Swath",
            "lat",
            "lon",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-mob_glo_phy-sss_mynrt_smos_P1D_202211",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-mob_glo_phy-sss_mynrt_smos_P1D_202211":
            if start is None:
                start = "2010-01-12T00:00:00Z"

            if end is None:
                end = "2023-10-24T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
