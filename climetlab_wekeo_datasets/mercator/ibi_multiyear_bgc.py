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
    "cmems_mod_ibi_bgc_my_0.083deg-3D-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_ibi_bgc_my_0.083deg-3D-climatology_P1M-m_202211
    "cmems_mod_ibi_bgc_my_0.083deg-3D_P1D-m_202012",  # noqa: E501 Cmems ibi reanalysis: daily biogeochemical products
    "cmems_mod_ibi_bgc_my_0.083deg-3D_P1M-m_202012",  # noqa: E501 Cmems ibi reanalysis: monthly biogeochemical products
    "cmems_mod_ibi_bgc_my_0.083deg-3D_P1Y-m_202211",  # noqa: E501 Cmems ibi reanalysis: yearly biogeochemical products
]


class ibi_multiyear_bgc(Main):
    name = "EO:MO:DAT:IBI_MULTIYEAR_BGC_005_003"
    dataset = "EO:MO:DAT:IBI_MULTIYEAR_BGC_005_003"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "chl",
            "chl_mean",
            "chl_standard_deviation",
            "depth",
            "dissic",
            "dissic_mean",
            "dissic_standard_deviation",
            "fe",
            "fe_mean",
            "fe_standard_deviation",
            "latitude",
            "longitude",
            "nh4",
            "nh4_mean",
            "nh4_standard_deviation",
            "no3",
            "no3_mean",
            "no3_standard_deviation",
            "nppv",
            "nppv_mean",
            "nppv_standard_deviation",
            "o2",
            "o2_mean",
            "o2_standard_deviation",
            "ph",
            "ph_mean",
            "ph_standard_deviation",
            "phyc",
            "phyc_mean",
            "phyc_standard_deviation",
            "po4",
            "po4_mean",
            "po4_standard_deviation",
            "si",
            "si_mean",
            "si_standard_deviation",
            "spco2",
            "spco2_mean",
            "spco2_standard_deviation",
            "time",
            "zeu",
            "zeu_mean",
            "zeu_standard_deviation",
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
        if layer == "cmems_mod_ibi_bgc_my_0.083deg-3D-climatology_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-28T00:00:00Z"

        if layer == "cmems_mod_ibi_bgc_my_0.083deg-3D_P1D-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_bgc_my_0.083deg-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_bgc_my_0.083deg-3D_P1Y-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
