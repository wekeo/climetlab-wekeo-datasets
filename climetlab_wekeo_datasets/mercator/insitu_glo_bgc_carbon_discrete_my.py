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
    "cmems_obs-ins_glo_bgc-car_my_glodap-obs_irr_202211",  # noqa: E501 cmems_obs-ins_glo_bgc-car_my_glodap-obs_irr_202211
    "cmems_obs-ins_glo_bgc-car_my_socat-obs_irr_202211",  # noqa: E501 cmems_obs-ins_glo_bgc-car_my_socat-obs_irr_202211
]


class insitu_glo_bgc_carbon_discrete_my(Main):
    name = "EO:MO:DAT:INSITU_GLO_BGC_CARBON_DISCRETE_MY_013_050"
    dataset = "EO:MO:DAT:INSITU_GLO_BGC_CARBON_DISCRETE_MY_013_050"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "ALKW",
            "ALKW_QC",
            "BATH",
            "BATH_QC",
            "CORG",
            "CORG_QC",
            "CPHL",
            "CPHL_QC",
            "DEPH",
            "DEPH_QC",
            "DOX2",
            "DOX2_QC",
            "FCO2",
            "FCO2_QC",
            "LATITUDE",
            "LONGITUDE",
            "NODW",
            "NODW_QC",
            "NT1D",
            "NT1D_QC",
            "NTAW",
            "NTAW_QC",
            "NTIW",
            "NTIW_QC",
            "PH25",
            "PH25_QC",
            "PHOW",
            "PHOW_QC",
            "PHPH",
            "PHPH_QC",
            "POSITION_QC",
            "PRES",
            "PRES_QC",
            "PSAL",
            "PSAL_QC",
            "SLCW",
            "SLCW_QC",
            "TEMP",
            "TEMP_QC",
            "TICW",
            "TICW_QC",
            "TIME",
            "TIME_QC",
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
        if layer == "cmems_obs-ins_glo_bgc-car_my_glodap-obs_irr_202211":
            if start is None:
                start = "1972-07-24T00:00:00Z"

            if end is None:
                end = "2021-11-16T00:00:00Z"

        if layer == "cmems_obs-ins_glo_bgc-car_my_socat-obs_irr_202211":
            if start is None:
                start = "1957-10-22T22:00:00Z"

            if end is None:
                end = "2021-12-30T09:28:20Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
