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
    "cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-asc-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-asc-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-asc-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-asc-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-des-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-des-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-des-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-des-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-asc-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-asc-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-asc-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-asc-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-des-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-des-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-des-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-des-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-asc-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-asc-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-asc-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-asc-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-des-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-des-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-des-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-des-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-asc-0.125deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-asc-0.125deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-asc-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-asc-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-des-0.125deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-des-0.125deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-des-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-des-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-asc-0.125deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-asc-0.125deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-asc-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-asc-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-des-0.125deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-des-0.125deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-des-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-des-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-asc-0.125deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-asc-0.125deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-asc-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-asc-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-des-0.125deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-des-0.125deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-des-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-des-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-oceansat3-oscat-asc-0.25deg_P1D-i_202406",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-oceansat3-oscat-asc-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-oceansat3-oscat-asc-0.5deg_P1D-i_202406",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-oceansat3-oscat-asc-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-oceansat3-oscat-des-0.25deg_P1D-i_202406",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-oceansat3-oscat-des-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-oceansat3-oscat-des-0.5deg_P1D-i_202406",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-oceansat3-oscat-des-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.5deg_P1D-i
]


class wind_glo_phy_l3_nrt(Main):
    name = "EO:MO:DAT:WIND_GLO_PHY_L3_NRT_012_002"
    dataset = "EO:MO:DAT:WIND_GLO_PHY_L3_NRT_012_002"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "air_density",
            "bs_distance",
            "eastward_model_stress",
            "eastward_stress",
            "eastward_wind",
            "measurement_time",
            "model_stress_curl",
            "model_stress_divergence",
            "model_stress_magnitude",
            "model_wind_to_dir",
            "northward_model_stress",
            "northward_stress",
            "northward_wind",
            "se_eastward_model_wind",
            "se_model_speed",
            "se_model_wind_curl",
            "se_model_wind_divergence",
            "se_northward_model_wind",
            "stress_curl",
            "stress_divergence",
            "wind_curl",
            "wind_divergence",
            "wind_speed",
            "wind_stress_magnitude",
            "wind_to_dir",
            "wvc_index",
            "wvc_quality_flag",
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
        end_datetime="2024-06-20T00:00:00Z",
        start_datetime="2016-01-01T00:00:00Z",
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
