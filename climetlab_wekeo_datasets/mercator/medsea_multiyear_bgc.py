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
    "cmems_mod_med_bgc-bio_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-bio_my_4.2km_P1Y-m
    "cmems_mod_med_bgc-bio_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-bio_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-car_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-car_my_4.2km_P1Y-m
    "cmems_mod_med_bgc-car_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-car_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-co2_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-co2_my_4.2km_P1Y-m
    "cmems_mod_med_bgc-co2_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-co2_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-nut_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-nut_my_4.2km_P1Y-m
    "cmems_mod_med_bgc-nut_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-nut_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-pft_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-pft_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-plankton_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-plankton_my_4.2km_P1Y-m
    "cmems_mod_med_bgc_my_4.2km_static_202211",  # noqa: E501 cmems_mod_med_bgc_my_4.2km_static
    "med-ogs-bio-rean-d_202105",  # noqa: E501 med-ogs-bio-rean-d
    "med-ogs-bio-rean-m_202105",  # noqa: E501 med-ogs-bio-rean-m
    "med-ogs-car-rean-d_202105",  # noqa: E501 med-ogs-car-rean-d
    "med-ogs-car-rean-m_202105",  # noqa: E501 med-ogs-car-rean-m
    "med-ogs-co2-rean-d_202105",  # noqa: E501 med-ogs-co2-rean-d
    "med-ogs-co2-rean-m_202105",  # noqa: E501 med-ogs-co2-rean-m
    "med-ogs-nut-rean-d_202105",  # noqa: E501 med-ogs-nut-rean-d
    "med-ogs-nut-rean-m_202105",  # noqa: E501 med-ogs-nut-rean-m
    "med-ogs-pft-rean-d_202105",  # noqa: E501 med-ogs-pft-rean-d
    "med-ogs-pft-rean-m_202105",  # noqa: E501 med-ogs-pft-rean-m
]


class medsea_multiyear_bgc(Main):
    name = "EO:MO:DAT:MEDSEA_MULTIYEAR_BGC_006_008"
    dataset = "EO:MO:DAT:MEDSEA_MULTIYEAR_BGC_006_008"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "dissic",
            "e1t",
            "e2t",
            "e3t",
            "fpco2",
            "latitude",
            "longitude",
            "nh4",
            "no3",
            "nppv",
            "o2",
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
        layer,
        bbox,
        max_date="2022-11-01T00:00:00Z",
        min_date="1999-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_med_bgc-bio_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-20T00:00:00Z"

        if layer == "cmems_mod_med_bgc-bio_myint_4.2km_P1M-m_202112":
            if min_date is None:
                min_date = "2021-07-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-car_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-20T00:00:00Z"

        if layer == "cmems_mod_med_bgc-car_myint_4.2km_P1M-m_202112":
            if min_date is None:
                min_date = "2021-07-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-co2_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-20T00:00:00Z"

        if layer == "cmems_mod_med_bgc-co2_myint_4.2km_P1M-m_202112":
            if min_date is None:
                min_date = "2021-07-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-nut_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-20T00:00:00Z"

        if layer == "cmems_mod_med_bgc-nut_myint_4.2km_P1M-m_202112":
            if min_date is None:
                min_date = "2021-07-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-pft_myint_4.2km_P1M-m_202112":
            if min_date is None:
                min_date = "2021-07-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-02-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-plankton_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-20T00:00:00Z"

        if layer == "cmems_mod_med_bgc_my_4.2km_static_202211":
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-28T00:00:00Z"

        if layer == "med-ogs-bio-rean-d_202105":
            if min_date is None:
                min_date = "1999-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-bio-rean-m_202105":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-car-rean-d_202105":
            if min_date is None:
                min_date = "1999-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-car-rean-m_202105":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-co2-rean-d_202105":
            if min_date is None:
                min_date = "1999-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-co2-rean-m_202105":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-nut-rean-d_202105":
            if min_date is None:
                min_date = "1999-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-nut-rean-m_202105":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-pft-rean-d_202105":
            if min_date is None:
                min_date = "1999-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-pft-rean-m_202105":
            if min_date is None:
                min_date = "1999-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
