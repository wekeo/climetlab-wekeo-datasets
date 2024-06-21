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
]


class sst_glo_sst_l3s_nrt_observations(Main):
    name = "EO:MO:DAT:SST_GLO_SST_L3S_NRT_OBSERVATIONS_010_010"
    dataset = "EO:MO:DAT:SST_GLO_SST_L3S_NRT_OBSERVATIONS_010_010"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "adjusted_sea_surface_temperature",
            "bias_to_reference_sst",
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
        end_datetime="2024-06-17T00:00:00Z",
        start_datetime="2020-12-31T00:00:00Z",
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
