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
    "bs-ulg-bio-int-m_202105",  # noqa: E501 Net primary production, dissolved oxygen (3d), bottom dissolved oxygen (2d) - daily mean
    "bs-ulg-bio-rean-d_202007",  # noqa: E501 Net primary production, dissolved oxygen (3d), bottom dissolved oxygen (2d) - daily mean
    "bs-ulg-bio-rean-m_202007",  # noqa: E501 Net primary production, dissolved oxygen (3d), bottom dissolved oxygen (2d) - daily mean
    "bs-ulg-car-int-m_202105",  # noqa: E501 Dissolved inorganic carbon, alkalinity, ph (3d) - daily mean
    "bs-ulg-car-rean-d_202007",  # noqa: E501 Dissolved inorganic carbon, alkalinity, ph (3d) - daily mean
    "bs-ulg-car-rean-m_202007",  # noqa: E501 Dissolved inorganic carbon, alkalinity, ph (3d) - daily mean
    "bs-ulg-co2-int-m_202105",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - daily mean
    "bs-ulg-co2-rean-d_202007",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - daily mean
    "bs-ulg-co2-rean-m_202007",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - daily mean
    "bs-ulg-nut-int-m_202105",  # noqa: E501 Nitrate and phosphate (3d) - daily mean
    "bs-ulg-nut-rean-d_202007",  # noqa: E501 Nitrate and phosphate (3d) - daily mean
    "bs-ulg-nut-rean-m_202007",  # noqa: E501 Nitrate and phosphate (3d) - daily mean
    "bs-ulg-pft-int-m_202105",  # noqa: E501 Phytoplankton carbon biomass and chlorophyll (3d) - daily mean
    "bs-ulg-pft-rean-d_202007",  # noqa: E501 Phytoplankton carbon biomass and chlorophyll (3d) - daily mean
    "bs-ulg-pft-rean-m_202007",  # noqa: E501 Phytoplankton carbon biomass and chlorophyll (3d) - daily mean
]


class blksea_reanalysis_bio(Main):
    name = "EO:MO:DAT:BLKSEA_REANALYSIS_BIO_007_005"
    dataset = "EO:MO:DAT:BLKSEA_REANALYSIS_BIO_007_005"

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
            "latitude",
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
        if layer == "bs-ulg-car-rean-d_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        if layer == "bs-ulg-nut-rean-m_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        if layer == "bs-ulg-pft-rean-m_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        if layer == "bs-ulg-nut-rean-d_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        if layer == "bs-ulg-bio-int-m_202105":
            if start is None:
                start = "2021-03-26T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "bs-ulg-car-rean-m_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        if layer == "bs-ulg-pft-int-m_202105":
            if start is None:
                start = "2021-03-26T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "bs-ulg-co2-rean-m_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        if layer == "bs-ulg-co2-rean-d_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        if layer == "bs-ulg-bio-rean-d_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        if layer == "bs-ulg-car-int-m_202105":
            if start is None:
                start = "2021-03-26T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "bs-ulg-co2-int-m_202105":
            if start is None:
                start = "2021-03-26T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "bs-ulg-nut-int-m_202105":
            if start is None:
                start = "2021-03-26T00:00:00Z"

            if end is None:
                end = "2023-09-14T00:00:00Z"

        if layer == "bs-ulg-bio-rean-m_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        if layer == "bs-ulg-pft-rean-d_202007":
            if start is None:
                start = "2020-05-19T00:00:00Z"

            if end is None:
                end = "2022-03-30T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
