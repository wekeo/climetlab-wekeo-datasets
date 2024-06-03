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
    "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.5deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.25deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.25deg_P1D-i
    "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.5deg_P1D-i_202311",  # noqa: E501 cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.5deg_P1D-i
]


class wind_glo_phy_l3_nrt(Main):
    name = "EO:MO:DAT:WIND_GLO_PHY_L3_NRT_012_002"
    dataset = "EO:MO:DAT:WIND_GLO_PHY_L3_NRT_012_002"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "air_density",
            "bs_distance",
            "eastward_model_stress",
            "eastward_stress",
            "eastward_wind",
            "lat",
            "lon",
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
            "time",
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
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-05-13T00:00:00Z",
        min_date="2016-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-asc-0.25deg_P1D-i_202311":
            if min_date is None:
                min_date = "2020-11-11T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-asc-0.5deg_P1D-i_202311":
            if min_date is None:
                min_date = "2020-11-11T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-des-0.25deg_P1D-i_202311":
            if min_date is None:
                min_date = "2020-11-11T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2b-hscat-des-0.5deg_P1D-i_202311":
            if min_date is None:
                min_date = "2020-11-11T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-asc-0.25deg_P1D-i_202311":
            if min_date is None:
                min_date = "2021-11-08T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-asc-0.5deg_P1D-i_202311":
            if min_date is None:
                min_date = "2021-11-08T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-des-0.25deg_P1D-i_202311":
            if min_date is None:
                min_date = "2021-11-08T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2c-hscat-des-0.5deg_P1D-i_202311":
            if min_date is None:
                min_date = "2021-11-08T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-asc-0.25deg_P1D-i_202311":
            if min_date is None:
                min_date = "2022-10-15T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-asc-0.5deg_P1D-i_202311":
            if min_date is None:
                min_date = "2022-10-15T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-des-0.25deg_P1D-i_202311":
            if min_date is None:
                min_date = "2022-10-15T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if layer == "cmems_obs-wind_glo_phy_nrt_l3-hy2d-hscat-des-0.5deg_P1D-i_202311":
            if min_date is None:
                min_date = "2022-10-15T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-asc-0.125deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2016-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2021-11-15T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-asc-0.25deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2016-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2021-11-15T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-des-0.125deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2016-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2021-11-15T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopa-ascat-des-0.25deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2016-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2021-11-15T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-asc-0.125deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2016-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-asc-0.25deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2016-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-des-0.125deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2016-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopb-ascat-des-0.25deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2016-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-asc-0.125deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2019-10-28T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-asc-0.25deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2019-10-28T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-des-0.125deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2019-10-28T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-metopc-ascat-des-0.25deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2019-10-28T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-13T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.25deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2018-10-21T00:00:00Z"

            if max_date is None:
                max_date = "2021-02-28T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-asc-0.5deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2018-10-21T00:00:00Z"

            if max_date is None:
                max_date = "2021-02-28T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.25deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2018-10-21T00:00:00Z"

            if max_date is None:
                max_date = "2021-02-28T00:00:00Z"

        if (
            layer
            == "cmems_obs-wind_glo_phy_nrt_l3-scatsat1-oscat-des-0.5deg_P1D-i_202311"
        ):
            if min_date is None:
                min_date = "2018-10-21T00:00:00Z"

            if max_date is None:
                max_date = "2021-02-28T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
