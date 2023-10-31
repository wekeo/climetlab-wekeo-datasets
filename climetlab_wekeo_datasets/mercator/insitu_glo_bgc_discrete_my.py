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
    "cmems_obs-ins_glo_bgc-chl_my_na_irr_202211",  # noqa: E501 cmems_obs-ins_glo_bgc-chl_my_na_irr_202211
    "cmems_obs-ins_glo_bgc-nut_my_na_irr_202211",  # noqa: E501 cmems_obs-ins_glo_bgc-nut_my_na_irr_202211
    "cmems_obs-ins_glo_bgc-ox_my_na_irr_202211",  # noqa: E501 cmems_obs-ins_glo_bgc-ox_my_na_irr_202211
]


class insitu_glo_bgc_discrete_my(Main):
    name = "EO:MO:DAT:INSITU_GLO_BGC_DISCRETE_MY_013_046"
    dataset = "EO:MO:DAT:INSITU_GLO_BGC_DISCRETE_MY_013_046"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "ALK3",
            "ALK3_QC",
            "C13D",
            "C13D_QC",
            "C14D",
            "C14D_QC",
            "CFC11",
            "CFC11_QC",
            "CFC12",
            "CFC12_QC",
            "CNDC",
            "CNDC_DM",
            "CNDC_QC",
            "DC_REFERENCE",
            "DENS",
            "DENS_QC",
            "DEPH",
            "DEPH_QC",
            "DIRECTION",
            "DOX1",
            "DOX1_QC",
            "DOX2",
            "DOX2_QC",
            "DOXY",
            "DOXY_QC",
            "FLU2",
            "FLU2_QC",
            "HELD",
            "HELD_QC",
            "HELM",
            "HELM_QC",
            "LATITUDE",
            "LONGITUDE",
            "NEON",
            "NEON_QC",
            "NTRA",
            "NTRA_QC",
            "OSAT",
            "OSAT_QC",
            "PHOS",
            "PHOS_QC",
            "PHPH",
            "PHPH_QC",
            "POSITION_QC",
            "PRES",
            "PRES_DM",
            "PRES_QC",
            "PSAL",
            "PSAL_DM",
            "PSAL_QC",
            "SIGMA_T",
            "SIGMA_T_QC",
            "SLCA",
            "SLCA_QC",
            "SVEL",
            "SVEL_QC",
            "TCO2",
            "TCO2_QC",
            "TEMP",
            "TEMP_DM",
            "TEMP_QC",
            "TIME",
            "TIME_QC",
            "TRIW",
            "TRIW_QC",
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
        if layer == "cmems_obs-ins_glo_bgc-chl_my_na_irr_202211":
            if start is None:
                start = "1905-08-01T03:00:00Z"

            if end is None:
                end = "2022-12-31T23:59:19Z"

        if layer == "cmems_obs-ins_glo_bgc-nut_my_na_irr_202211":
            if start is None:
                start = "1901-01-01T08:00:00Z"

            if end is None:
                end = "2022-12-31T23:24:00Z"

        if layer == "cmems_obs-ins_glo_bgc-ox_my_na_irr_202211":
            if start is None:
                start = "1901-01-01T08:00:00Z"

            if end is None:
                end = "2022-12-31T23:24:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
