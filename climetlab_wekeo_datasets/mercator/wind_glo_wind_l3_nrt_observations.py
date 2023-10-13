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
    "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_ASC_V2_202012",  # noqa: E501 Global ocean - wind - hy-2b hscat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_DES_V2_202012",  # noqa: E501 Global ocean - wind - hy-2b hscat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_ASC_V2_202012",  # noqa: E501 Global ocean - wind - hy-2b hscat - 50km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_DES_V2_202012",  # noqa: E501 Global ocean - wind - hy-2b hscat - 50km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_ASC_V2_202112",  # noqa: E501 Global ocean - wind - hy-2c hscat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_DES_V2_202112",  # noqa: E501 Global ocean - wind - hy-2c hscat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_ASC_V2_202112",  # noqa: E501 Global ocean - wind - hy-2c hscat - 50km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_DES_V2_202112",  # noqa: E501 Global ocean - wind - hy-2c hscat - 50km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2D_HSCAT_25_ASC_V2_202211",  # noqa: E501 Global ocean - wind - hy-2d hscat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2D_HSCAT_25_DES_V2_202211",  # noqa: E501 Global ocean - wind - hy-2d hscat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2D_HSCAT_50_ASC_V2_202211",  # noqa: E501 Global ocean - wind - hy-2d hscat - 50km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_HY-2D_HSCAT_50_DES_V2_202211",  # noqa: E501 Global ocean - wind - hy-2d hscat - 50km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_12_ASC_V2",  # noqa: E501 Global ocean - wind - metop-a ascat - 12km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_12_DES_V2",  # noqa: E501 Global ocean - wind - metop-a ascat - 12km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_25_ASC_V2",  # noqa: E501 Global ocean - wind - metop-a ascat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_25_DES_V2",  # noqa: E501 Global ocean - wind - metop-a ascat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_ASC_V2",  # noqa: E501 Global ocean - wind - metop-b ascat - 12km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_DES_V2",  # noqa: E501 Global ocean - wind - metop-b ascat - 12km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_ASC_V2",  # noqa: E501 Global ocean - wind - metop-b ascat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_DES_V2",  # noqa: E501 Global ocean - wind - metop-b ascat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_ASC_V2_201912",  # noqa: E501 Global ocean - wind - metop-c ascat - 12km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_DES_V2_201912",  # noqa: E501 Global ocean - wind - metop-c ascat - 12km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_ASC_V2_201912",  # noqa: E501 Global ocean - wind - metop-c ascat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_DES_V2_201912",  # noqa: E501 Global ocean - wind - metop-c ascat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_25_ASC_V2_201811",  # noqa: E501 Global ocean - wind - scatsat-1 oscat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_25_DES_V2_201811",  # noqa: E501 Global ocean - wind - scatsat-1 oscat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_50_ASC_V2_201811",  # noqa: E501 Global ocean - wind - scatsat-1 oscat - 50km daily ascending v2
    "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_50_DES_V2_201811",  # noqa: E501 Global ocean - wind - scatsat-1 oscat - 50km daily descending v2
]


class wind_glo_wind_l3_nrt_observations(Main):
    name = "EO:MO:DAT:WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002"
    dataset = "EO:MO:DAT:WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
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
        if layer == "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_25_ASC_V2_201811":
            if start is None:
                start = "2018-10-21T00:00:00Z"

            if end is None:
                end = "2021-02-28T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_25_DES_V2_201811":
            if start is None:
                start = "2018-10-21T00:00:00Z"

            if end is None:
                end = "2021-02-28T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_ASC_V2_201912":
            if start is None:
                start = "2019-10-28T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_ASC_V2_202012":
            if start is None:
                start = "2020-11-11T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_DES_V2_202012":
            if start is None:
                start = "2020-11-11T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_DES_V2":
            if start is None:
                start = "2016-01-01T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_DES_V2_201912":
            if start is None:
                start = "2019-10-28T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_50_ASC_V2_201811":
            if start is None:
                start = "2018-10-21T00:00:00Z"

            if end is None:
                end = "2021-02-28T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_ASC_V2":
            if start is None:
                start = "2016-01-01T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2D_HSCAT_50_DES_V2_202211":
            if start is None:
                start = "2022-10-15T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2D_HSCAT_50_ASC_V2_202211":
            if start is None:
                start = "2022-10-15T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_12_DES_V2":
            if start is None:
                start = "2016-01-01T00:00:00Z"

            if end is None:
                end = "2021-11-15T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_ASC_V2":
            if start is None:
                start = "2016-01-01T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_ASC_V2_201912":
            if start is None:
                start = "2019-10-28T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_DES_V2":
            if start is None:
                start = "2016-01-01T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_DES_V2_202012":
            if start is None:
                start = "2020-11-11T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_50_DES_V2_201811":
            if start is None:
                start = "2018-10-21T00:00:00Z"

            if end is None:
                end = "2021-02-28T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_25_DES_V2":
            if start is None:
                start = "2016-01-01T00:00:00Z"

            if end is None:
                end = "2021-11-15T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2D_HSCAT_25_ASC_V2_202211":
            if start is None:
                start = "2022-10-15T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_DES_V2_202112":
            if start is None:
                start = "2021-11-08T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2D_HSCAT_25_DES_V2_202211":
            if start is None:
                start = "2022-10-15T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_DES_V2_202112":
            if start is None:
                start = "2021-11-08T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_ASC_V2_202012":
            if start is None:
                start = "2020-11-11T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_DES_V2_201912":
            if start is None:
                start = "2019-10-28T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_ASC_V2_202112":
            if start is None:
                start = "2021-11-08T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_25_ASC_V2":
            if start is None:
                start = "2016-01-01T00:00:00Z"

            if end is None:
                end = "2021-11-15T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_ASC_V2_202112":
            if start is None:
                start = "2021-11-08T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_12_ASC_V2":
            if start is None:
                start = "2016-01-01T00:00:00Z"

            if end is None:
                end = "2021-11-15T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
