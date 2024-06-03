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
    "OSISAF-GLO-SEAICE_CONC_TIMESERIES-NH-LA-OBS_202003",  # noqa: E501 OSISAF-GLO-SEAICE_CONC_TIMESERIES-NH-LA-OBS_202003
    "OSISAF-GLO-SEAICE_CONC_TIMESERIES-SH-LA-OBS_202003",  # noqa: E501 OSISAF-GLO-SEAICE_CONC_TIMESERIES-SH-LA-OBS_202003
]


class seaice_glo_seaice_l4_rep_observations(Main):
    name = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_REP_OBSERVATIONS_011_009"
    dataset = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_REP_OBSERVATIONS_011_009"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "Lambert_Azimuthal_Grid",
            "algorithm_standard_uncertainty",
            "ice_conc",
            "lat",
            "lon",
            "raw_ice_conc_values",
            "smearing_standard_uncertainty",
            "status_flag",
            "time",
            "time_bnds",
            "total_standard_uncertainty",
            "xc",
            "yc",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2021-01-01T00:00:00Z",
        min_date="1978-10-25T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-NH-LA-OBS_202003":
            if min_date is None:
                min_date = "2021-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-20T12:00:00Z"

        if layer == "OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-SH-LA-OBS_202003":
            if min_date is None:
                min_date = "2021-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-20T12:00:00Z"

        if layer == "OSISAF-GLO-SEAICE_CONC_TIMESERIES-NH-LA-OBS_202003":
            if min_date is None:
                min_date = "1978-10-25T00:00:00Z"

            if max_date is None:
                max_date = "2021-01-01T00:00:00Z"

        if layer == "OSISAF-GLO-SEAICE_CONC_TIMESERIES-SH-LA-OBS_202003":
            if min_date is None:
                min_date = "1978-10-25T00:00:00Z"

            if max_date is None:
                max_date = "2021-01-01T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
