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
]


class medsea_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_BGC_006_014"
    dataset = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_BGC_006_014"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "chl",
            "diatoC",
            "diatoChla",
            "dinoC",
            "dinoChla",
            "dissic",
            "fgco2",
            "kd490",
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
            "zooc",
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
        end_datetime="2024-06-27T00:00:00Z",
        start_datetime="2020-01-01T00:00:00Z",
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
