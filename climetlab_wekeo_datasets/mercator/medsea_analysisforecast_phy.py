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
    "cmems_mod_med_phy-cur_anfc_4.2km_P1D-m_202211",  # noqa: E501 Horizontal velocity (3d) - daily mean
    "cmems_mod_med_phy-cur_anfc_4.2km_P1M-m_202211",  # noqa: E501 Horizontal velocity (3d) - monthly mean
    "cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i_202211",  # noqa: E501 Horizontal surface velocity (2d) - 15 minutes instantaneous
    "cmems_mod_med_phy-cur_anfc_4.2km_PT1H-m_202211",  # noqa: E501 Horizontal velocity (3d) - hourly mean
    "cmems_mod_med_phy-cur_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 Horizontal velocity (3d) - hourly mean - time series
    "cmems_mod_med_phy-mld_anfc_4.2km_P1D-m_202211",  # noqa: E501 Mixed layer depth (2d) - daily mean
    "cmems_mod_med_phy-mld_anfc_4.2km_P1M-m_202211",  # noqa: E501 Mixed layer depth (2d) - monthly mean
    "cmems_mod_med_phy-mld_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 Mixed layer depth (2d) - hourly mean - time series
    "cmems_mod_med_phy-sal_anfc_4.2km_P1D-m_202211",  # noqa: E501 Salinity (3d) - daily mean
    "cmems_mod_med_phy-sal_anfc_4.2km_P1M-m_202211",  # noqa: E501 Salinity (3d) - monthly mean
    "cmems_mod_med_phy-sal_anfc_4.2km_PT1H-m_202211",  # noqa: E501 Salinity (3d) - hourly mean
    "cmems_mod_med_phy-sal_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 Salinity (3d) - hourly mean - time series
    "cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m_202211",  # noqa: E501 Sea surface height (2d) - daily mean
    "cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m_202211",  # noqa: E501 Sea surface height (2d) - monthly mean
    "cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i_202211",  # noqa: E501 Sea surface height (2d) - 15 minutes instantaneous
    "cmems_mod_med_phy-ssh_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 Sea surface height (2d) - hourly mean - time series
    "cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202211",  # noqa: E501 Sea temperature (3d) - daily mean
    "cmems_mod_med_phy-tem_anfc_4.2km_P1M-m_202211",  # noqa: E501 Sea temperature (3d) - monthly mean
    "cmems_mod_med_phy-tem_anfc_4.2km_PT1H-m_202211",  # noqa: E501 Sea temperature (3d) - hourly mean
    "cmems_mod_med_phy-tem_anfc_4.2km_PT1HTS-m_202211",  # noqa: E501 Sea temperature (3d) - hourly mean - time series
    "cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m_202211",  # noqa: E501 Vertical velocity (3d) - daily mean
    "cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m_202211",  # noqa: E501 Vertical velocity (3d) - monthly mean
]


class medsea_analysisforecast_phy(Main):
    name = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_PHY_006_013"
    dataset = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_PHY_006_013"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "lat",
            "lon",
            "mlotst",
            "so",
            "thetao",
            "time",
            "uo",
            "vo",
            "wo",
            "zos",
            "zos_detided",
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
        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_P1D-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_P1M-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-09-12T00:00:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_PT15M-i_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_PT1H-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-cur_anfc_4.2km_PT1HTS-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-mld_anfc_4.2km_P1D-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-mld_anfc_4.2km_P1M-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-09-12T00:00:00Z"

        if layer == "cmems_mod_med_phy-mld_anfc_4.2km_PT1HTS-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_P1D-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_P1M-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-09-12T00:00:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_PT1H-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-sal_anfc_4.2km_PT1HTS-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_P1D-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_P1M-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-09-12T00:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_PT15M-i_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_anfc_4.2km_PT1HTS-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_P1D-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_P1M-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-09-12T00:00:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_PT1H-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-tem_anfc_4.2km_PT1HTS-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-wcur_anfc_4.2km_P1D-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-10-28T00:00:00Z"

        if layer == "cmems_mod_med_phy-wcur_anfc_4.2km_P1M-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2023-09-12T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
