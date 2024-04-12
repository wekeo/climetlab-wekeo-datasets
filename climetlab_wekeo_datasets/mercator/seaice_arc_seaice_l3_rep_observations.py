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
    "cmems_obs-si_arc_phy_my_drift-amsr_P2D_202012",  # noqa: E501 Arctic ocean - sea ice - 2 days drift, amsr
    "cmems_obs-si_arc_phy_my_drift-amsr_P3D_202012",  # noqa: E501 Arctic ocean - sea ice - 3 days drift, amsr
    "cmems_obs-si_arc_phy_my_drift-amsr_P6D_202012",  # noqa: E501 Arctic ocean - sea ice - 6 days drift, amsr
]


class seaice_arc_seaice_l3_rep_observations(Main):
    name = "EO:MO:DAT:SEAICE_ARC_SEAICE_L3_REP_OBSERVATIONS_011_010"
    dataset = "EO:MO:DAT:SEAICE_ARC_SEAICE_L3_REP_OBSERVATIONS_011_010"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "depth",
            "eastward_sea_ice_velocity",
            "latitude",
            "longitude",
            "northward_sea_ice_velocity",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2012-04-30T00:00:00Z",
        min_date="1999-10-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if (
            layer
            == "CERSAT-GLO-SEAICE_30DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311"
        ):
            if min_date is None:
                min_date = "2007-02-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-01T00:00:00Z"

        if (
            layer
            == "CERSAT-GLO-SEAICE_30DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311"
        ):
            if min_date is None:
                min_date = "1999-10-01T00:00:00Z"

            if max_date is None:
                max_date = "2012-04-01T00:00:00Z"

        if (
            layer
            == "CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE_202311"
        ):
            if min_date is None:
                min_date = "2007-01-31T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-30T00:00:00Z"

        if (
            layer
            == "CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311"
        ):
            if min_date is None:
                min_date = "2007-01-31T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-30T00:00:00Z"

        if (
            layer
            == "CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE_202311"
        ):
            if min_date is None:
                min_date = "1999-09-28T00:00:00Z"

            if max_date is None:
                max_date = "2009-11-18T00:00:00Z"

        if (
            layer
            == "CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311"
        ):
            if min_date is None:
                min_date = "1999-10-01T00:00:00Z"

            if max_date is None:
                max_date = "2012-04-30T00:00:00Z"

        if (
            layer
            == "CERSAT-GLO-SEAICE_6DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE_202311"
        ):
            if min_date is None:
                min_date = "2007-01-31T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-30T00:00:00Z"

        if (
            layer
            == "CERSAT-GLO-SEAICE_6DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE_202311"
        ):
            if min_date is None:
                min_date = "1999-09-25T00:00:00Z"

            if max_date is None:
                max_date = "2009-11-15T00:00:00Z"

        if layer == "cmems_obs-si_arc_phy-drift_my_l3-ssmi_P30D_202311":
            if min_date is None:
                min_date = "1992-01-01T00:00:00Z"

            if max_date is None:
                max_date = "1999-12-01T00:00:00Z"

        if layer == "cmems_obs-si_arc_phy-drift_my_l3-ssmi_P3D_202311":
            if min_date is None:
                min_date = "1991-12-03T00:00:00Z"

            if max_date is None:
                max_date = "2000-01-03T00:00:00Z"

        if layer == "cmems_obs-si_arc_phy_my_drift-amsr_P2D_202012":
            if min_date is None:
                min_date = "2002-10-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-05-02T00:00:00Z"

        if layer == "cmems_obs-si_arc_phy_my_drift-amsr_P3D_202012":
            if min_date is None:
                min_date = "2002-10-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-05-03T00:00:00Z"

        if layer == "cmems_obs-si_arc_phy_my_drift-amsr_P6D_202012":
            if min_date is None:
                min_date = "2002-10-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-05-06T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
