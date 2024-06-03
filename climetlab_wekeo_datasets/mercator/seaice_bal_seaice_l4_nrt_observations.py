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
    "cmems_obs-si_bal_phy-sit_nrt_x-500m-l4_P1D_202311",  # noqa: E501 cmems_obs-si_bal_phy-sit_nrt_x-500m-l4_P1D_202311
    "cmems_sat-si_bal_conc_nrt_500m_d_202007",  # noqa: E501 cmems_sat-si_bal_conc_nrt_500m_d_202007
    "cmems_sat-si_bal_thick_nrt_500m_hi_202012",  # noqa: E501 cmems_sat-si_bal_thick_nrt_500m_hi_202012
    "FMI-BAL-SEAICE_DRIFT-SAR-NRT-OBS",  # noqa: E501 FMI-BAL-SEAICE_DRIFT-SAR-NRT-OBS
    "FMI-BAL-SEAICE_THICK-MOSAIC-SAR-NRT-OBS",  # noqa: E501 FMI-BAL-SEAICE_THICK-MOSAIC-SAR-NRT-OBS
    "FMI-BAL-SEAICE_THICK-SAR-NRT-OBS",  # noqa: E501 FMI-BAL-SEAICE_THICK-SAR-NRT-OBS
]


class seaice_bal_seaice_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SEAICE_BAL_SEAICE_L4_NRT_OBSERVATIONS_011_011"
    dataset = "EO:MO:DAT:SEAICE_BAL_SEAICE_L4_NRT_OBSERVATIONS_011_011"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "crs",
            "ice_concentration",
            "ice_concentration_uncertainty",
            "ice_drift_quality",
            "ice_thickness",
            "lat",
            "lon",
            "sea_ice_thickness",
            "sea_ice_x_displacement",
            "sea_ice_y_displacement",
            "time",
            "time_bnds",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-05-06T16:56:21Z",
        min_date="2023-05-11T15:56:18Z",
        variables=None,
        limit=None,
    ):
        if layer == "FMI-BAL-SEAICE_DRIFT-SAR-NRT-OBS":
            if min_date is None:
                min_date = "2018-01-04T04:57:59Z"

            if max_date is None:
                max_date = "2024-05-06T03:48:30Z"

        if layer == "FMI-BAL-SEAICE_THICK-MOSAIC-SAR-NRT-OBS":
            if min_date is None:
                min_date = "2017-12-25T16:18:59Z"

            if max_date is None:
                max_date = "2024-05-06T18:00:00Z"

        if layer == "FMI-BAL-SEAICE_THICK-SAR-NRT-OBS":
            if min_date is None:
                min_date = "2018-01-01T04:45:26Z"

            if max_date is None:
                max_date = "2024-05-06T05:04:23Z"

        if layer == "cmems_obs-si_bal_phy-sit_nrt_x-500m-l4_P1D_202311":
            if min_date is None:
                min_date = "2023-05-11T15:56:18Z"

            if max_date is None:
                max_date = "2024-05-06T16:56:21Z"

        if layer == "cmems_sat-si_bal_conc_nrt_500m_d_202007":
            if min_date is None:
                min_date = "2020-03-22T04:56:16Z"

            if max_date is None:
                max_date = "2024-05-06T05:00:00Z"

        if layer == "cmems_sat-si_bal_thick_nrt_500m_hi_202012":
            if min_date is None:
                min_date = "2019-02-09T04:48:37Z"

            if max_date is None:
                max_date = "2024-05-06T16:15:18Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
