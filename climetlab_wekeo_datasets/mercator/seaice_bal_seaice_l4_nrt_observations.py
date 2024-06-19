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
    "FMI-BAL-SEAICE_CONC-L4-NRT-OBS",  # noqa: E501 FMI-BAL-SEAICE_CONC-L4-NRT-OBS
    "FMI-BAL-SEAICE_THICK-L4-NRT-OBS",  # noqa: E501 FMI-BAL-SEAICE_THICK-L4-NRT-OBS
]


class seaice_bal_seaice_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SEAICE_BAL_SEAICE_L4_NRT_OBSERVATIONS_011_004"
    dataset = "EO:MO:DAT:SEAICE_BAL_SEAICE_L4_NRT_OBSERVATIONS_011_004"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "concentration_range",
            "ice_concentration",
            "ice_thickness",
            "product_quality",
            "thickness_range",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        end_datetime="2024-06-05T00:00:00Z",
        start_datetime="2018-01-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
