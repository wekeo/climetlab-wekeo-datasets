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
    "cmems_obs-ins_glo_phy-cur_my_adcp_irr_202211",  # noqa: E501 cmems_obs-ins_glo_phy-cur_my_adcp_irr_202211
    "cmems_obs-ins_glo_phy-cur_my_drifter_PT6H_202211",  # noqa: E501 cmems_obs-ins_glo_phy-cur_my_drifter_PT6H_202211
    "cmems_obs-ins_glo_phy-cur_my_radar-radial_irr_202211",  # noqa: E501 cmems_obs-ins_glo_phy-cur_my_radar-radial_irr_202211
    "cmems_obs-ins_glo_phy-cur_my_radar-total_irr_202211",  # noqa: E501 cmems_obs-ins_glo_phy-cur_my_radar-total_irr_202211
]


class insitu_glo_phy_uv_discrete_my(Main):
    name = "EO:MO:DAT:INSITU_GLO_PHY_UV_DISCRETE_MY_013_044"
    dataset = "EO:MO:DAT:INSITU_GLO_PHY_UV_DISCRETE_MY_013_044"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "AVRB_QC",
            "CSPD_QC",
            "DC_REFERENCE",
            "DDNS_QC",
            "DEPH",
            "DEPH_QC",
            "DRVA",
            "EACC",
            "EWCS",
            "EWCT",
            "EWCT_QC",
            "EWCT_WS",
            "EWCT_WS_QC",
            "GDOP",
            "GDOP_QC",
            "HCSS",
            "LATITUDE",
            "LONGITUDE",
            "MDFL_QC",
            "NARX",
            "NATX",
            "NSCS",
            "NSCT",
            "NSCT_QC",
            "NSCT_WS",
            "NSCT_WS_QC",
            "OWTR_QC",
            "POSITION_QC",
            "QCflag",
            "RDCT_QC",
            "RDVA",
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
            "TEMP",
            "TEMP_QC",
            "TIME",
            "TIME_QC",
            "UACC",
            "VACC",
            "VART_QC",
            "VCSP",
            "VCSP_QC",
            "WS_TYPE_OF_PROCESSING",
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
        if layer == "cmems_obs-ins_glo_phy-cur_my_drifter_PT6H_202211":
            if start is None:
                start = "1990-01-01T00:00:00Z"

            if end is None:
                end = "2022-11-07T00:00:00Z"

        if layer == "cmems_obs-ins_glo_phy-cur_my_radar-radial_irr_202211":
            if start is None:
                start = "2008-12-31T23:30:00Z"

            if end is None:
                end = "2021-12-31T23:30:00Z"

        if layer == "cmems_obs-ins_glo_phy-cur_my_radar-total_irr_202211":
            if start is None:
                start = "2009-01-11T23:30:00Z"

            if end is None:
                end = "2021-12-31T23:30:00Z"

        if layer == "cmems_obs-ins_glo_phy-cur_my_adcp_irr_202211":
            if start is None:
                start = "2001-01-04T16:47:52Z"

            if end is None:
                end = "2021-11-16T21:30:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
