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
    "cmems_mod_med_bgc-bio_my_4.2km_P1Y-m_202211",  # noqa: E501 Primary production and oxygen (3d) - yearly mean
    "cmems_mod_med_bgc-bio_myint_4.2km_P1M-m_202112",  # noqa: E501 Primary production and oxygen (3d) - monthly mean
    "cmems_mod_med_bgc-car_my_4.2km_P1Y-m_202211",  # noqa: E501 Dissolved inorganic carbon, ph and alkalinity (3d) - yearly mean
    "cmems_mod_med_bgc-car_myint_4.2km_P1M-m_202112",  # noqa: E501 Dissolved inorganic carbon, ph and alkalinity (3d) - monthly mean
    "cmems_mod_med_bgc-co2_my_4.2km_P1Y-m_202211",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - yearly mean
    "cmems_mod_med_bgc-co2_myint_4.2km_P1M-m_202112",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - monthly mean
    "cmems_mod_med_bgc-nut_my_4.2km_P1Y-m_202211",  # noqa: E501 Nitrate, phosphate and ammonium (3d) - yearly mean
    "cmems_mod_med_bgc-nut_myint_4.2km_P1M-m_202112",  # noqa: E501 Nitrate, phosphate and ammonium (3d) - monthly mean
    "cmems_mod_med_bgc-pft_myint_4.2km_P1M-m_202112",  # noqa: E501 Phytoplankton carbon biomass and chlorophyll (3d) - monthly mean
    "cmems_mod_med_bgc-plankton_my_4.2km_P1Y-m_202211",  # noqa: E501 Phytoplankton carbon biomass and chlorophyll (3d) - yearly mean
    "med-ogs-bio-rean-d_202105",  # noqa: E501 Primary production and oxygen (3d) - daily mean
    "med-ogs-bio-rean-m_202105",  # noqa: E501 Primary production and oxygen (3d) - monthly mean
    "med-ogs-car-rean-d_202105",  # noqa: E501 Dissolved inorganic carbon, ph and alkalinity (3d) - daily mean
    "med-ogs-car-rean-m_202105",  # noqa: E501 Dissolved inorganic carbon, ph and alkalinity (3d) - monthly mean
    "med-ogs-co2-rean-d_202105",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - daily mean
    "med-ogs-co2-rean-m_202105",  # noqa: E501 Surface partial pressure of co2 and surface co2 flux (2d) - monthly mean
    "med-ogs-nut-rean-d_202105",  # noqa: E501 Nitrate, phosphate and ammonium (3d) - daily mean
    "med-ogs-nut-rean-m_202105",  # noqa: E501 Nitrate, phosphate and ammonium (3d) - monthly mean
    "med-ogs-pft-rean-d_202105",  # noqa: E501 Phytoplankton carbon biomass and chlorophyll (3d) - daily mean
    "med-ogs-pft-rean-m_202105",  # noqa: E501 Phytoplankton carbon biomass and chlorophyll (3d) - monthly mean
]


class medsea_multiyear_bgc(Main):
    name = "EO:MO:DAT:MEDSEA_MULTIYEAR_BGC_006_008"
    dataset = "EO:MO:DAT:MEDSEA_MULTIYEAR_BGC_006_008"

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
        if layer == "med-ogs-pft-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-car-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-car_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-08-01T00:00:00Z"

        if layer == "med-ogs-co2-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-nut_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        if layer == "cmems_mod_med_bgc-co2_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-02-21T00:00:00Z"

            if end is None:
                end = "2023-08-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-car_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        if layer == "med-ogs-bio-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-nut-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-plankton_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        if layer == "med-ogs-nut-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-pft-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-bio_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        if layer == "cmems_mod_med_bgc-bio_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-08-01T00:00:00Z"

        if layer == "med-ogs-co2-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-car-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-co2_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        if layer == "med-ogs-bio-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-pft_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-08-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-nut_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-03-21T00:00:00Z"

            if end is None:
                end = "2023-08-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
