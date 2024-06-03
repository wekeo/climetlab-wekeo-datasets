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
    "cmems_mod_med_phy-cur_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-cur_anfc_4.2km-3D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km-3D_PT1H-m
    "cmems_mod_med_phy-cur_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_P1D-m_202211
    "cmems_mod_med_phy-cur_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-cur_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_P1M-m_202211
    "cmems_mod_med_phy-cur_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i_202211",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i_202211
    "cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i
    "cmems_mod_med_phy-cur_anfc_4.2km_PT1H-m_202211",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_PT1H-m_202211
    "cmems_mod_med_phy-cur_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 cmems_mod_med_phy-cur_anfc_4.2km_PT1HTS-m_202211
    "cmems_mod_med_phy-cur_anfc_detided_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-cur_anfc_detided_4.2km_P1D-m
    "cmems_mod_med_phy-mld_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-mld_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-mld_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_phy-mld_anfc_4.2km_P1D-m_202211
    "cmems_mod_med_phy-mld_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-mld_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-mld_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_phy-mld_anfc_4.2km_P1M-m_202211
    "cmems_mod_med_phy-mld_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-mld_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-mld_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 cmems_mod_med_phy-mld_anfc_4.2km_PT1HTS-m_202211
    "cmems_mod_med_phy-sal_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-sal_anfc_4.2km-3D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km-3D_PT1H-m
    "cmems_mod_med_phy-sal_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km_P1D-m_202211
    "cmems_mod_med_phy-sal_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-sal_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km_P1M-m_202211
    "cmems_mod_med_phy-sal_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-sal_anfc_4.2km_PT1H-m_202211",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km_PT1H-m_202211
    "cmems_mod_med_phy-sal_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 cmems_mod_med_phy-sal_anfc_4.2km_PT1HTS-m_202211
    "cmems_mod_med_phy-ssh_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m_202211
    "cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m_202211
    "cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i_202211",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i_202211
    "cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i
    "cmems_mod_med_phy-ssh_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_4.2km_PT1HTS-m_202211
    "cmems_mod_med_phy-ssh_anfc_detided_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-ssh_anfc_detided_4.2km_P1D-m
    "cmems_mod_med_phy-tem_anfc_4.2km-2D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km-2D_PT1H-m
    "cmems_mod_med_phy-tem_anfc_4.2km-3D_PT1H-m_202311",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km-3D_PT1H-m
    "cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202211
    "cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-tem_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km_P1M-m_202211
    "cmems_mod_med_phy-tem_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km_P1M-m
    "cmems_mod_med_phy-tem_anfc_4.2km_PT1H-m_202211",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km_PT1H-m_202211
    "cmems_mod_med_phy-tem_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 cmems_mod_med_phy-tem_anfc_4.2km_PT1HTS-m_202211
    "cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m_202211",  # noqa: E501 cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m_202211
    "cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m_202311",  # noqa: E501 cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m
    "cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m_202211",  # noqa: E501 cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m_202211
    "cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m_202311",  # noqa: E501 cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m
    "cmems_mod_med_phy_anfc_4.2km_static_202211",  # noqa: E501 cmems_mod_med_phy_anfc_4.2km_static_202211
    "cmems_mod_med_phy_anfc_4.2km_static_202311",  # noqa: E501 cmems_mod_med_phy_anfc_4.2km_static
]


class medsea_analysisforecast_phy(Main):
    name = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_PHY_006_013"
    dataset = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_PHY_006_013"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "e1t",
            "e2t",
            "e3t",
            "lat",
            "latitude",
            "lon",
            "longitude",
            "mdt",
            "mlotst",
            "so",
            "thetao",
            "time",
            "uo",
            "uo_detided",
            "vo",
            "vo_detided",
            "wo",
            "zos",
            "zos_detided",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-04-16T00:00:00Z",
        min_date="2021-11-16T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_med_phy-cur_anfc_4.2km-2D_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-11-01T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km-3D_PT1H-m_202311":
            if min_date is None:
                min_date = "2023-11-13T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-24T23:30:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2022-01-22T12:00:00Z"

            if max_date is None:
                max_date = "2024-03-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2021-03-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-16T12:00:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i_202211":
            if min_date is None:
                min_date = "2022-01-22T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-24T23:45:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i_202311":
            if min_date is None:
                min_date = "2021-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-24T23:45:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_PT1H-m_202211":
            if min_date is None:
                min_date = "2022-10-17T00:30:00Z"

            if max_date is None:
                max_date = "2024-03-24T23:30:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_PT1HTS-m_202211":
            if min_date is None:
                min_date = "2022-01-22T00:30:00Z"

            if max_date is None:
                max_date = "2024-03-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_detided_4.2km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_med_phy-mld_anfc_4.2km-2D_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-11-01T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-mld_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2022-01-22T12:00:00Z"

            if max_date is None:
                max_date = "2024-03-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-mld_anfc_4.2km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-mld_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2021-03-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-16T12:00:00Z"

        if layer == "cmems_mod_med_phy-mld_anfc_4.2km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_med_phy-mld_anfc_4.2km_PT1HTS-m_202211":
            if min_date is None:
                min_date = "2022-01-22T00:30:00Z"

            if max_date is None:
                max_date = "2024-03-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km-2D_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-11-01T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km-3D_PT1H-m_202311":
            if min_date is None:
                min_date = "2023-11-13T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-24T23:30:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2022-01-22T12:00:00Z"

            if max_date is None:
                max_date = "2024-03-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2021-03-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-16T12:00:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_PT1H-m_202211":
            if min_date is None:
                min_date = "2022-10-17T00:30:00Z"

            if max_date is None:
                max_date = "2024-03-24T23:30:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_PT1HTS-m_202211":
            if min_date is None:
                min_date = "2022-01-22T00:30:00Z"

            if max_date is None:
                max_date = "2024-03-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km-2D_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-11-01T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2022-01-22T12:00:00Z"

            if max_date is None:
                max_date = "2024-03-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2021-03-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-16T12:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i_202211":
            if min_date is None:
                min_date = "2022-01-22T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-24T23:45:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i_202311":
            if min_date is None:
                min_date = "2021-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-24T23:45:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_PT1HTS-m_202211":
            if min_date is None:
                min_date = "2022-01-22T00:30:00Z"

            if max_date is None:
                max_date = "2024-03-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_detided_4.2km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km-2D_PT1H-m_202311":
            if min_date is None:
                min_date = "2021-11-01T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km-3D_PT1H-m_202311":
            if min_date is None:
                min_date = "2023-11-13T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-24T23:30:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2022-01-22T12:00:00Z"

            if max_date is None:
                max_date = "2024-03-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2021-03-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-16T12:00:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_PT1H-m_202211":
            if min_date is None:
                min_date = "2022-10-17T00:30:00Z"

            if max_date is None:
                max_date = "2024-03-24T23:30:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_PT1HTS-m_202211":
            if min_date is None:
                min_date = "2022-01-22T00:30:00Z"

            if max_date is None:
                max_date = "2024-03-29T23:30:00Z"

        if layer == "cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m_202211":
            if min_date is None:
                min_date = "2022-01-22T12:00:00Z"

            if max_date is None:
                max_date = "2024-03-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-29T12:00:00Z"

        if layer == "cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m_202211":
            if min_date is None:
                min_date = "2021-03-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-16T12:00:00Z"

        if layer == "cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_med_phy_anfc_4.2km_static_202211":
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-28T00:00:00Z"

        if layer == "cmems_mod_med_phy_anfc_4.2km_static_202311":
            if min_date is None:
                min_date = "2023-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-28T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
