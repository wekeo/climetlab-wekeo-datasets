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
    "KNMI-GLO-WIND_L3-REP-OBS_ERS-1_SCAT_25_ASC_202007",  # noqa: E501 Global ocean - wind - ers-1 scat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_ERS-1_SCAT_25_DES_202007",  # noqa: E501 Global ocean - wind - ers-1 scat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-REP-OBS_ERS-2_SCAT_25_ASC_202007",  # noqa: E501 Global ocean - wind - ers-2 scat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_ERS-2_SCAT_25_DES_202007",  # noqa: E501 Global ocean - wind - ers-2 scat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-REP-OBS_METOP-A_ASCAT_12_ASC_202007",  # noqa: E501 Global ocean - wind - metop-a ascat - 12km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_METOP-A_ASCAT_12_DES_202007",  # noqa: E501 Global ocean - wind - metop-a ascat - 12km daily descending v2
    "KNMI-GLO-WIND_L3-REP-OBS_METOP-A_ASCAT_25_ASC_202007",  # noqa: E501 Global ocean - wind - metop-a ascat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_METOP-A_ASCAT_25_DES_202007",  # noqa: E501 Global ocean - wind - metop-a ascat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-REP-OBS_METOP-B_ASCAT_12_ASC_202112",  # noqa: E501 Global ocean - wind - metop-b ascat - 12km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_METOP-B_ASCAT_12_DES_202112",  # noqa: E501 Global ocean - wind - metop-b ascat - 12km daily descending v2
    "KNMI-GLO-WIND_L3-REP-OBS_METOP-B_ASCAT_25_ASC_202112",  # noqa: E501 Global ocean - wind - metop-b ascat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_METOP-B_ASCAT_25_DES_202112",  # noqa: E501 Global ocean - wind - metop-b ascat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-REP-OBS_OCEANSAT2_OSCAT_25_ASC_202007",  # noqa: E501 Global ocean - wind - oceanscat2 oscat - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_OCEANSAT2_OSCAT_25_DES_202007",  # noqa: E501 Global ocean - wind - oceanscat2 oscat - 25km daily descending v2
    "KNMI-GLO-WIND_L3-REP-OBS_OCEANSAT2_OSCAT_50_ASC_202007",  # noqa: E501 Global ocean - wind - oceanscat2 oscat - 50km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_OCEANSAT2_OSCAT_50_DES_202007",  # noqa: E501 Global ocean - wind - oceanscat2 oscat - 50km daily descending v2
    "KNMI-GLO-WIND_L3-REP-OBS_QUIKSCAT_SEAWINDS_25_ASC_202007",  # noqa: E501 Global ocean - wind - quikscat seawinds - 25km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_QUIKSCAT_SEAWINDS_25_DES_202007",  # noqa: E501 Global ocean - wind - quikscat seawinds - 25km daily descending v2
    "KNMI-GLO-WIND_L3-REP-OBS_QUIKSCAT_SEAWINDS_50_ASC_202007",  # noqa: E501 Global ocean - wind - quikscat seawinds - 50km daily ascending v2
    "KNMI-GLO-WIND_L3-REP-OBS_QUIKSCAT_SEAWINDS_50_DES_202007",  # noqa: E501 Global ocean - wind - quikscat seawinds - 50km daily descending v2
]


class wind_glo_wind_l3_rep_observations(Main):
    name = "EO:MO:DAT:WIND_GLO_WIND_L3_REP_OBSERVATIONS_012_005"
    dataset = "EO:MO:DAT:WIND_GLO_WIND_L3_REP_OBSERVATIONS_012_005"

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
        if layer == "KNMI-GLO-WIND_L3-REP-OBS_ERS-1_SCAT_25_ASC_202007":
            if start is None:
                start = "1992-03-02T00:00:00Z"

            if end is None:
                end = "1996-06-03T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_ERS-1_SCAT_25_DES_202007":
            if start is None:
                start = "1992-03-02T00:00:00Z"

            if end is None:
                end = "1996-06-03T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_ERS-2_SCAT_25_ASC_202007":
            if start is None:
                start = "1996-03-20T00:00:00Z"

            if end is None:
                end = "2001-01-15T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_ERS-2_SCAT_25_DES_202007":
            if start is None:
                start = "1996-03-20T00:00:00Z"

            if end is None:
                end = "2001-01-15T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_METOP-A_ASCAT_12_ASC_202007":
            if start is None:
                start = "2007-01-01T00:00:00Z"

            if end is None:
                end = "2021-11-15T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_METOP-A_ASCAT_12_DES_202007":
            if start is None:
                start = "2007-01-01T00:00:00Z"

            if end is None:
                end = "2021-11-15T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_METOP-A_ASCAT_25_ASC_202007":
            if start is None:
                start = "2007-01-01T00:00:00Z"

            if end is None:
                end = "2021-11-15T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_METOP-A_ASCAT_25_DES_202007":
            if start is None:
                start = "2007-01-01T00:00:00Z"

            if end is None:
                end = "2021-11-15T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_METOP-B_ASCAT_12_ASC_202112":
            if start is None:
                start = "2019-01-01T00:00:00Z"

            if end is None:
                end = "2023-06-30T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_METOP-B_ASCAT_12_DES_202112":
            if start is None:
                start = "2019-01-01T00:00:00Z"

            if end is None:
                end = "2023-06-30T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_METOP-B_ASCAT_25_ASC_202112":
            if start is None:
                start = "2019-01-01T00:00:00Z"

            if end is None:
                end = "2023-06-30T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_METOP-B_ASCAT_25_DES_202112":
            if start is None:
                start = "2019-01-01T00:00:00Z"

            if end is None:
                end = "2023-06-30T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_OCEANSAT2_OSCAT_25_ASC_202007":
            if start is None:
                start = "2009-12-15T00:00:00Z"

            if end is None:
                end = "2014-02-20T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_OCEANSAT2_OSCAT_25_DES_202007":
            if start is None:
                start = "2009-12-15T00:00:00Z"

            if end is None:
                end = "2014-02-20T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_OCEANSAT2_OSCAT_50_ASC_202007":
            if start is None:
                start = "2009-12-15T00:00:00Z"

            if end is None:
                end = "2014-02-20T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_OCEANSAT2_OSCAT_50_DES_202007":
            if start is None:
                start = "2009-12-15T00:00:00Z"

            if end is None:
                end = "2014-02-20T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_QUIKSCAT_SEAWINDS_25_ASC_202007":
            if start is None:
                start = "1999-07-19T00:00:00Z"

            if end is None:
                end = "2009-11-21T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_QUIKSCAT_SEAWINDS_25_DES_202007":
            if start is None:
                start = "1999-07-19T00:00:00Z"

            if end is None:
                end = "2009-11-21T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_QUIKSCAT_SEAWINDS_50_ASC_202007":
            if start is None:
                start = "1999-07-19T00:00:00Z"

            if end is None:
                end = "2009-11-21T00:00:00Z"

        if layer == "KNMI-GLO-WIND_L3-REP-OBS_QUIKSCAT_SEAWINDS_50_DES_202007":
            if start is None:
                start = "2003-11-23T00:00:00Z"

            if end is None:
                end = "2009-11-21T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
