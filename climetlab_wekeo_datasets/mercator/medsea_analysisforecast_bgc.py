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
    "cmems_mod_med_bgc-bio_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_bgc-bio_anfc_4.2km_P1D-m
    "cmems_mod_med_bgc-bio_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_bgc-bio_anfc_4.2km_P1M-m
    "cmems_mod_med_bgc-car_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_bgc-car_anfc_4.2km_P1D-m
    "cmems_mod_med_bgc-car_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_bgc-car_anfc_4.2km_P1M-m
    "cmems_mod_med_bgc-co2_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_bgc-co2_anfc_4.2km_P1D-m
    "cmems_mod_med_bgc-co2_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_bgc-co2_anfc_4.2km_P1M-m
    "cmems_mod_med_bgc-nut_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_bgc-nut_anfc_4.2km_P1D-m
    "cmems_mod_med_bgc-nut_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_bgc-nut_anfc_4.2km_P1M-m
    "cmems_mod_med_bgc-optics_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_bgc-optics_anfc_4.2km_P1D-m
    "cmems_mod_med_bgc-optics_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_bgc-optics_anfc_4.2km_P1M-m
    "cmems_mod_med_bgc-pft_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_bgc-pft_anfc_4.2km_P1D-m
    "cmems_mod_med_bgc-pft_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_bgc-pft_anfc_4.2km_P1M-m
    "cmems_mod_med_bgc_anfc_4.2km_static_202211",  # noqa: E501 cmems_mod_med_bgc_anfc_4.2km_static
]


class medsea_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_BGC_006_014"
    dataset = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_BGC_006_014"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "deptho",
            "deptho_lev",
            "diatoC",
            "diatoChla",
            "dinoC",
            "dinoChla",
            "dissic",
            "fgco2",
            "kd490",
            "latitude",
            "longitude",
            "mask",
            "nanoC",
            "nanoChla",
            "nh4",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "picoC",
            "picoChla",
            "po4",
            "si",
            "spco2",
            "talk",
            "time",
            "zooc",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-02-01T00:00:00Z",
        min_date="2020-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_med_bgc-bio_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2020-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_med_bgc-bio_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-car_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2020-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_med_bgc-car_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-co2_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2020-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_med_bgc-co2_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-nut_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2020-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_med_bgc-nut_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-optics_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2020-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_med_bgc-optics_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2020-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-pft_anfc_4.2km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-10-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-11T12:00:00Z"

        if layer == "cmems_mod_med_bgc-pft_anfc_4.2km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-10-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc_anfc_4.2km_static_202211":
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-28T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
