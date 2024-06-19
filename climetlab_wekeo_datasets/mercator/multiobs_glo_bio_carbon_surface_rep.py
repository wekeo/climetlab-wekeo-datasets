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
    "dataset-carbon-rep-monthly_202311",  # noqa: E501 dataset-carbon-rep-monthly
]


class multiobs_glo_bio_carbon_surface_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_BIO_CARBON_SURFACE_REP_015_008"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_BIO_CARBON_SURFACE_REP_015_008"

    @normalize(
        "variables",
        [
            "fgco2",
            "fgco2_uncertainty",
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
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        variables,
        layer="dataset-carbon-rep-monthly_202311",
        bbox=None,
        end_datetime="2022-12-01T00:00:00Z",
        start_datetime="1985-01-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            variables=variables,
            layer=layer,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
