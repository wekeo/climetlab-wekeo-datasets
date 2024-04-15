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

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        bbox,
        layer="cmems_obs-mob_glo_phy-sss_mynrt_smos_P1D_202211",
        max_date="2024-04-01T12:00:00Z",
        min_date="2010-01-12T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-mob_glo_phy-sss_mynrt_smos_P1D_202211":
            if min_date is None:
                min_date = "2010-01-12T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
