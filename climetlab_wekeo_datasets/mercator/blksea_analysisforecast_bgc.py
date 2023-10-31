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
    "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202211",  # noqa: E501 Net primary production, dissolved oxygen (3d), bottom dissolved oxygen (2d) - daily mean
    "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202211",  # noqa: E501 Net primary production, dissolved oxygen (3d), bottom dissolved oxygen (2d) - monthly mean
    "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202211",  # noqa: E501 Dissolved inorganic carbon, alkalinity, ph (3d) - daily mean
    "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202211",  # noqa: E501 Dissolved inorganic carbon, alkalinity, ph (3d) - monthly mean
    "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202211",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - daily mean
    "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202211",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - monthly mean
    "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202211",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - hourly mean
    "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202211",  # noqa: E501 Nitrate and phosphate (3d) - daily mean
    "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202211",  # noqa: E501 Nitrate and phosphate (3d) - monthly mean
    "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202211",  # noqa: E501 Photosynthetical-active radiation and attenuation coefficient (3d) - daily mean
    "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202211",  # noqa: E501 Photosynthetical-active radiation and attenuation coefficient (3d) - monthly mean
    "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202211",  # noqa: E501 Phytoplankton carbon biomass and chlorophyll (3d) - daily mean
    "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202211",  # noqa: E501 Phytoplankton carbon biomass and chlorophyll (3d) - monthly mean
]


class blksea_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"
    dataset = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "dissic",
            "fpco2",
            "kd",
            "latitude",
            "lght",
            "longitude",
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
        if layer == "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-10-04T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-10-04T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-10-04T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-10-04T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-10-04T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-10-04T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
