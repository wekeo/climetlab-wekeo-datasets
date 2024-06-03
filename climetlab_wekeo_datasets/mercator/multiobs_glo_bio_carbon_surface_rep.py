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
    "dataset-carbon-rep-monthly_202211",  # noqa: E501 dataset-carbon-rep-monthly_202211
    "dataset-carbon-rep-monthly_202311",  # noqa: E501 dataset-carbon-rep-monthly
]


class multiobs_glo_bio_carbon_surface_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_BIO_CARBON_SURFACE_REP_015_008"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_BIO_CARBON_SURFACE_REP_015_008"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "fgco2",
            "fgco2_uncertainty",
            "latitude",
            "longitude",
            "omega_ar",
            "omega_ar_uncertainty",
            "omega_ca",
            "omega_ca_uncertainty",
            "ph",
            "ph_uncertainty",
            "spco2",
            "spco2_uncertainty",
            "talk",
            "talk_uncertainty",
            "tco2",
            "tco2_uncertainty",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2021-12-15T00:00:00Z",
        min_date="1985-01-15T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "dataset-carbon-rep-monthly_202211":
            if min_date is None:
                min_date = "1985-01-15T00:00:00Z"

            if max_date is None:
                max_date = "2021-12-15T00:00:00Z"

        if layer == "dataset-carbon-rep-monthly_202311":
            if min_date is None:
                min_date = "2023-08-21T00:00:00Z"

            if max_date is None:
                max_date = "2023-08-21T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
