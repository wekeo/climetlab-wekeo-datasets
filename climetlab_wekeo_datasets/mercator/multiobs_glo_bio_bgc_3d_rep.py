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
    "cmems_obs_glo_bgc3d_rep_weekly_202112",  # noqa: E501 cmems_obs_glo_bgc3d_rep_weekly
]


class multiobs_glo_bio_bgc_3d_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_BIO_BGC_3D_REP_015_010"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_BIO_BGC_3D_REP_015_010"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        layer,
        bbox,
        max_date="2023-01-03T00:00:00Z",
        min_date="1998-01-07T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs_glo_bgc3d_rep_clim_202112":
            if min_date is None:
                min_date = "2021-09-06T00:00:00Z"

            if max_date is None:
                max_date = "2021-09-06T00:00:00Z"

        if layer == "cmems_obs_glo_bgc3d_rep_weekly_202112":
            if min_date is None:
                min_date = "1998-01-07T00:00:00Z"

            if max_date is None:
                max_date = "2023-01-03T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
