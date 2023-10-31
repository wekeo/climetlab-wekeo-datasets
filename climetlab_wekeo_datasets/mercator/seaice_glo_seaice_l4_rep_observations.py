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
    "OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-NH-LA-OBS_202003",  # noqa: E501 Interim sea ice concentration climate data record version 3 from the eumetsat osi saf
    "OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-SH-LA-OBS_202003",  # noqa: E501 Interim sea ice concentration climate data record version 3 from the eumetsat osi saf
    "OSISAF-GLO-SEAICE_CONC_TIMESERIES-NH-LA-OBS_202003",  # noqa: E501 Sea ice concentration climate data record version 3 (smmr, ssm/i, and ssmis) from the eumetsat osi saf
    "OSISAF-GLO-SEAICE_CONC_TIMESERIES-SH-LA-OBS_202003",  # noqa: E501 Sea ice concentration climate data record version 3 (smmr, ssm/i, and ssmis) from the eumetsat osi saf
]


class seaice_glo_seaice_l4_rep_observations(Main):
    name = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_REP_OBSERVATIONS_011_009"
    dataset = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_REP_OBSERVATIONS_011_009"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
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
        if layer == "OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-NH-LA-OBS_202003":
            if start is None:
                start = "2021-01-01T00:00:00Z"

            if end is None:
                end = "2023-10-10T00:00:00Z"

        if layer == "OSISAF-GLO-SEAICE_CONC_CONT_TIMESERIES-SH-LA-OBS_202003":
            if start is None:
                start = "2021-01-01T00:00:00Z"

            if end is None:
                end = "2023-10-10T00:00:00Z"

        if layer == "OSISAF-GLO-SEAICE_CONC_TIMESERIES-NH-LA-OBS_202003":
            if start is None:
                start = "1978-10-25T00:00:00Z"

            if end is None:
                end = "2021-01-01T00:00:00Z"

        if layer == "OSISAF-GLO-SEAICE_CONC_TIMESERIES-SH-LA-OBS_202003":
            if start is None:
                start = "1978-10-25T00:00:00Z"

            if end is None:
                end = "2021-01-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
