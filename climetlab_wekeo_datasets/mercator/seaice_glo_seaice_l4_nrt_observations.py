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
    "METNO-GLO-SEAICE_DRIFT-NORTH-L4-NRT-OBS",  # noqa: E501 Arctic ice drift, l4 osisaf, 62km daily (metno-glo-seaice drift-north-l4-nrt-obs)
    "METNO-GLO-SEAICE_DRIFT-SOUTH-L4-NRT-OBS",  # noqa: E501 Antarctic ice drift, l4 osisaf, 62km daily (metno-glo-seaice drift-south-l4-nrt-obs)
    "osisaf_obs-si_glo_phy-sic-north_nrt_amsr2_l4_P1D-m_202304",  # noqa: E501 Arctic amsr2 ice concentration, l4 osisaf, 10km daily
    "osisaf_obs-si_glo_phy-sic-north_nrt_ssmis_l4_P1D-m_202304",  # noqa: E501 Arctic ice concentration, l4 osisaf, 10km daily (metno-glo-seaice conc-north-l4-nrt-obs)
    "osisaf_obs-si_glo_phy-sic-south_nrt_amsr2_l4_P1D-m_202304",  # noqa: E501 Antarctic amsr2 ice concentration, l4 osisaf, 10km daily
    "osisaf_obs-si_glo_phy-sic-south_nrt_ssmis_l4_P1D-m_202304",  # noqa: E501 Antarctic ice concentration, l4 osisaf, 10km daily (metno-glo-seaice conc-south-l4-nrt-obs)
    "osisaf_obs-si_glo_phy-siedge_nrt_nh-P1D_202107",  # noqa: E501 Daily sea ice edge analysis from osi saf eumetsat
    "osisaf_obs-si_glo_phy-siedge_nrt_sh-P1D_202107",  # noqa: E501 Daily sea ice edge analysis from osi saf eumetsat
    "osisaf_obs-si_glo_phy-sitype_nrt_nh-P1D_202107",  # noqa: E501 Daily sea ice type analysis from osi saf eumetsat
    "osisaf_obs-si_glo_phy-sitype_nrt_sh-P1D_202107",  # noqa: E501 Daily sea ice type analysis from osi saf eumetsat
]


class seaice_glo_seaice_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_NRT_OBSERVATIONS_011_001"
    dataset = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_NRT_OBSERVATIONS_011_001"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "Polar_Stereographic_Grid",
            "algorithm_uncertainty",
            "dX",
            "dY",
            "dt0",
            "dt1",
            "ice_conc",
            "ice_edge",
            "ice_type",
            "lat",
            "lat1",
            "lon",
            "lon1",
            "orbit_num_amsr",
            "orbit_num_ascat",
            "orbit_num_ssmis",
            "param_used",
            "raw_ice_conc_values",
            "smearing_uncertainty",
            "status_flag",
            "time",
            "time_bnds",
            "total_uncertainty",
            "uncert_dX_and_dY",
            "uncertainty",
            "xc",
            "yc",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-04-01T12:00:00Z",
        min_date="2023-03-23T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "METNO-GLO-SEAICE_DRIFT-NORTH-L4-NRT-OBS":
            if min_date is None:
                min_date = "2017-12-30T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "METNO-GLO-SEAICE_DRIFT-SOUTH-L4-NRT-OBS":
            if min_date is None:
                min_date = "2017-12-30T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-sic-north_nrt_amsr2_l4_P1D-m_202304":
            if min_date is None:
                min_date = "2023-03-23T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-sic-north_nrt_ssmis_l4_P1D-m_202304":
            if min_date is None:
                min_date = "2023-03-23T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-sic-south_nrt_amsr2_l4_P1D-m_202304":
            if min_date is None:
                min_date = "2023-03-23T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-sic-south_nrt_ssmis_l4_P1D-m_202304":
            if min_date is None:
                min_date = "2023-03-23T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-siedge_nrt_nh-P1D_202107":
            if min_date is None:
                min_date = "2021-06-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-siedge_nrt_sh-P1D_202107":
            if min_date is None:
                min_date = "2021-06-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-sitype_nrt_nh-P1D_202107":
            if min_date is None:
                min_date = "2021-06-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-sitype_nrt_sh-P1D_202107":
            if min_date is None:
                min_date = "2021-06-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-01T12:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
