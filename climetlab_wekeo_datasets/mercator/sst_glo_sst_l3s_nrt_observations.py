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
    "cmems_obs-sst_glo_phy_l3s_gir_P1D-m_202311",  # noqa: E501 cmems_obs-sst_glo_phy_l3s_gir_P1D-m
    "cmems_obs-sst_glo_phy_l3s_pir_P1D-m_202311",  # noqa: E501 cmems_obs-sst_glo_phy_l3s_pir_P1D-m
    "cmems_obs-sst_glo_phy_l3s_pmw_P1D-m_202311",  # noqa: E501 cmems_obs-sst_glo_phy_l3s_pmw_P1D-m
    "IFREMER-GLOB-SST-L3-NRT-OBS_FULL_TIME_SERIE_202211",  # noqa: E501 IFREMER-GLOB-SST-L3-NRT-OBS_FULL_TIME_SERIE
    "IFREMER-GLOB-SST-L3-NRT-OBS_FULL_TIME_SERIE_202211",  # noqa: E501 Odyssea global sea surface temperature gridded level 3s daily multi-sensor observations
]


class sst_glo_sst_l3s_nrt_observations(Main):
    name = "EO:MO:DAT:SST_GLO_SST_L3S_NRT_OBSERVATIONS_010_010"
    dataset = "EO:MO:DAT:SST_GLO_SST_L3S_NRT_OBSERVATIONS_010_010"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "adjusted_sea_surface_temperature",
            "bias_to_reference_sst",
            "lat",
            "lon",
            "or_latitude",
            "or_longitude",
            "or_number_of_pixels",
            "quality_level",
            "satellite_zenith_angle",
            "sea_surface_temperature",
            "sea_surface_temperature_stddev",
            "solar_zenith_angle",
            "sources_of_sst",
            "sses_bias",
            "sses_standard_deviation",
            "sst_dtime",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2023-12-10T12:00:00Z",
        min_date="2020-12-31T12:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "IFREMER-GLOB-SST-L3-NRT-OBS_FULL_TIME_SERIE_202211":
            if min_date is None:
                min_date = "2020-12-31T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-10T12:00:00Z"

        if layer == "cmems_obs-sst_glo_phy_l3s_gir_P1D-m_202311":
            if min_date is None:
                min_date = "2020-12-31T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-10T12:00:00Z"

        if layer == "cmems_obs-sst_glo_phy_l3s_pir_P1D-m_202311":
            if min_date is None:
                min_date = "2020-12-31T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-10T12:00:00Z"

        if layer == "cmems_obs-sst_glo_phy_l3s_pmw_P1D-m_202311":
            if min_date is None:
                min_date = "2020-12-31T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-10T12:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
