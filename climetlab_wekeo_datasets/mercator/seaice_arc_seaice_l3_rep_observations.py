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
    "CERSAT-GLO-SEAICE_30DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_30DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_30DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_30DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_6DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_6DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_6DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_6DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE
    "cmems_obs-si_arc_phy-drift_my_l3-ssmi_P30D_202311",  # noqa: E501 cmems_obs-si_arc_phy-drift_my_l3-ssmi_P30D
    "cmems_obs-si_arc_phy-drift_my_l3-ssmi_P3D_202311",  # noqa: E501 cmems_obs-si_arc_phy-drift_my_l3-ssmi_P3D
]


class seaice_arc_seaice_l3_rep_observations(Main):
    name = "EO:MO:DAT:SEAICE_ARC_SEAICE_L3_REP_OBSERVATIONS_011_010"
    dataset = "EO:MO:DAT:SEAICE_ARC_SEAICE_L3_REP_OBSERVATIONS_011_010"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "eastward_sea_ice_velocity",
            "northward_sea_ice_velocity",
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
        end_datetime="2012-04-01T00:00:00Z",
        start_datetime="1999-10-01T00:00:00Z",
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
