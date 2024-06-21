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
    "OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-NH-LA-OBS_202003",  # noqa: E501 OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-NH-LA-OBS
    "OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-SH-LA-OBS_202003",  # noqa: E501 OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-SH-LA-OBS
]


class seaice_glo_seaice_l4_rep_observations(Main):
    name = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_REP_OBSERVATIONS_011_009"
    dataset = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_REP_OBSERVATIONS_011_009"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "algorithm_standard_uncertainty",
            "ice_conc",
            "raw_ice_conc_values",
            "smearing_standard_uncertainty",
            "status_flag",
            "total_standard_uncertainty",
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
        end_datetime="2024-06-03T00:00:00Z",
        start_datetime="2021-01-01T00:00:00Z",
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
