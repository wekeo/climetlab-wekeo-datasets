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
    "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202211
    "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-bio_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202211
    "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-bio_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202211
    "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-car_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202211
    "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-car_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202211
    "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202211
    "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202211",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202211
    "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202311",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m
    "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202211
    "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-nut_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202211
    "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-nut_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202211
    "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-opt_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202211
    "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-opt_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202211
    "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-pft_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202211
    "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-pft_anfc_3km_P1M-m
    "cmems_mod_blk_bgc_anfc_3km_static_202211",  # noqa: E501 cmems_mod_blk_bgc_anfc_3km_static_202211
    "cmems_mod_blk_bgc_anfc_3km_static_202311",  # noqa: E501 cmems_mod_blk_bgc_anfc_3km_static
]


class blksea_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"
    dataset = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "deptho",
            "deptho_lev",
            "dissic",
            "fpco2",
            "kd",
            "latitude",
            "lght",
            "longitude",
            "mask",
            "no3",
            "nppv",
            "o2",
            "o2b",
            "ph",
            "phyc",
            "po4",
            "spco2",
            "talk",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-04-11T12:00:00Z",
        min_date="2021-08-05T12:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202211":
            if min_date is None:
                min_date = "2021-08-05T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202311":
            if min_date is None:
                min_date = "2022-01-24T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202211":
            if min_date is None:
                min_date = "2021-08-05T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202311":
            if min_date is None:
                min_date = "2022-01-24T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202211":
            if min_date is None:
                min_date = "2021-08-05T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202311":
            if min_date is None:
                min_date = "2022-01-24T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202211":
            if min_date is None:
                min_date = "2022-11-01T00:30:00Z"

            if max_date is None:
                max_date = "2024-04-11T23:30:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202311":
            if min_date is None:
                min_date = "2022-01-24T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-28T23:30:00Z"

        if layer == "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202211":
            if min_date is None:
                min_date = "2021-08-05T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202311":
            if min_date is None:
                min_date = "2022-01-24T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202211":
            if min_date is None:
                min_date = "2021-08-05T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202311":
            if min_date is None:
                min_date = "2022-01-24T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202211":
            if min_date is None:
                min_date = "2021-08-05T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202311":
            if min_date is None:
                min_date = "2022-01-24T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2023-12-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-15T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_blk_bgc_anfc_3km_static_202211":
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-28T00:00:00Z"

        if layer == "cmems_mod_blk_bgc_anfc_3km_static_202311":
            if min_date is None:
                min_date = "2023-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-28T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
