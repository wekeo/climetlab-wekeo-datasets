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
    "cmems_obs-ins_glo_phy-cur_nrt_argo_irr_202211",  # noqa: E501 cmems_obs-ins_glo_phy-cur_nrt_argo_irr_202211
    "cmems_obs-ins_glo_phy-cur_nrt_drifter_irr_202211",  # noqa: E501 cmems_obs-ins_glo_phy-cur_nrt_drifter_irr_202211
    "cmems_obs-ins_glo_phy-cur_nrt_radar-radial_irr_202211",  # noqa: E501 cmems_obs-ins_glo_phy-cur_nrt_radar-radial_irr_202211
    "cmems_obs-ins_glo_phy-cur_nrt_radar-total_irr_202211",  # noqa: E501 cmems_obs-ins_glo_phy-cur_nrt_radar-total_irr_202211
]


class insitu_glo_phy_uv_discrete_nrt(Main):
    name = "EO:MO:DAT:INSITU_GLO_PHY_UV_DISCRETE_NRT_013_048"
    dataset = "EO:MO:DAT:INSITU_GLO_PHY_UV_DISCRETE_NRT_013_048"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "AVRB_QC",
            "BEAR",
            "CCOV",
            "CSPD_QC",
            "CURRENT_TEST",
            "CURRENT_TEST_QC",
            "CYCLE_NUMBER",
            "DC_REFERENCE",
            "DDNS_QC",
            "DEPH",
            "DEPH_QC",
            "DRVA",
            "DURATION",
            "ERSC",
            "ERTC",
            "ESPC",
            "ETMP",
            "EWCS",
            "EWCT",
            "EWCT_QC",
            "GDOP",
            "GDOP_QC",
            "GROUNDED",
            "LATITUDE",
            "LONGITUDE",
            "MAXV",
            "MDFL_QC",
            "MINV",
            "NARX",
            "NATX",
            "NSCS",
            "NSCT",
            "NSCT_QC",
            "OWTR_QC",
            "POSITION_QC",
            "PRES",
            "PRES_QC",
            "QCflag",
            "RDCT_QC",
            "RDVA",
            "RNGE",
            "SCDR",
            "SCDT",
            "SDN_CRUISE",
            "SDN_EDMO_CODE",
            "SDN_LOCAL_CDI_ID",
            "SDN_REFERENCES",
            "SDN_STATION",
            "SDN_XLINK",
            "SLNR",
            "SLNT",
            "SLTR",
            "SLTT",
            "SPRC",
            "TEMP",
            "TEMP_QC",
            "TIME",
            "TIME_QC",
            "VART_QC",
            "WSPE_MODEL",
            "WSPE_MODEL_QC",
            "WSPN_MODEL",
            "WSPN_MODEL_QC",
            "WSTE_MODEL",
            "WSTE_MODEL_QC",
            "WSTN_MODEL",
            "WSTN_MODEL_QC",
            "XDST",
            "YDST",
            "crs",
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
        if layer == "cmems_obs-ins_glo_phy-cur_nrt_argo_irr_202211":
            if start is None:
                start = "1997-07-20T07:27:03Z"

            if end is None:
                end = "2023-06-22T08:28:05Z"

        if layer == "cmems_obs-ins_glo_phy-cur_nrt_drifter_irr_202211":
            if start is None:
                start = "1986-06-02T09:00:00Z"

            if end is None:
                end = "2023-06-25T12:00:00Z"

        if layer == "cmems_obs-ins_glo_phy-cur_nrt_radar-radial_irr_202211":
            if start is None:
                start = "2016-06-22T10:30:00Z"

            if end is None:
                end = "2023-06-27T21:45:00Z"

        if layer == "cmems_obs-ins_glo_phy-cur_nrt_radar-total_irr_202211":
            if start is None:
                start = "2012-03-20T00:45:00Z"

            if end is None:
                end = "2023-06-27T20:35:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
