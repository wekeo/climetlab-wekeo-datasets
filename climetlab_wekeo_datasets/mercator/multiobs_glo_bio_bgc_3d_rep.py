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
    "cmems_obs_glo_bgc3d_rep_clim_202112",  # noqa: E501 Global ocean 3d chlorophyll-a concentration, particulate backscattering coeffient and particulate organic carbon monthly climatology
    "cmems_obs_glo_bgc3d_rep_weekly_202112",  # noqa: E501 Global ocean 3d chlorophyll-a concentration, particulate backscattering coeffient and particulate organic carbon
]


class multiobs_glo_bio_bgc_3d_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_BIO_BGC_3D_REP_015_010"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_BIO_BGC_3D_REP_015_010"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "bbp",
            "bbp_error",
            "chl",
            "chl_error",
            "depth",
            "latitude",
            "longitude",
            "poc",
            "poc_error",
            "time",
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
        if layer == "cmems_obs_glo_bgc3d_rep_clim_202112":
            if start is None:
                start = "2021-09-06T00:00:00Z"

            if end is None:
                end = "2021-09-06T00:00:00Z"

        if layer == "cmems_obs_glo_bgc3d_rep_weekly_202112":
            if start is None:
                start = "1998-01-07T00:00:00Z"

            if end is None:
                end = "2020-12-30T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
