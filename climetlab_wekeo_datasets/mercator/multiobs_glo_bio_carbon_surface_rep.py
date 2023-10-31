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
    "dataset-carbon-rep-monthly_202211",  # noqa: E501 Surface ocean carbon fields
]


class multiobs_glo_bio_carbon_surface_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_BIO_CARBON_SURFACE_REP_015_008"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_BIO_CARBON_SURFACE_REP_015_008"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
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
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="dataset-carbon-rep-monthly_202211",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "dataset-carbon-rep-monthly_202211":
            if start is None:
                start = "2022-09-30T00:00:00Z"

            if end is None:
                end = "2022-09-30T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
