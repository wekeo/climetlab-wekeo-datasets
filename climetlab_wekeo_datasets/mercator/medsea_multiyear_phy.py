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
    "cmems_mod_med_phy-cur_my_4.2km_P1Y-m_202211",  # noqa: E501 Horizontal velocity (3d) - yearly mean
    "cmems_mod_med_phy-mld_my_4.2km_P1Y-m_202211",  # noqa: E501 Mixed layer depth (2d) - yearly mean
    "cmems_mod_med_phy-sal_my_4.2km_P1Y-m_202211",  # noqa: E501 Salinity (3d) - yearly
    "cmems_mod_med_phy-ssh_my_4.2km_P1Y-m_202211",  # noqa: E501 Sea surface height (2d) - yearly mean
    "cmems_mod_med_phy-tem_my_4.2km_P1Y-m_202211",  # noqa: E501 Potential temperature (3d) - yearly mean
    "cmems_mod_med_phy_my_4.2km-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_med_phy_my_4.2km-climatology_P1M-m_202211
    "med-cmcc-cur-int-m_202112",  # noqa: E501 Horizontal velocity (3d) - monthly mean
    "med-cmcc-cur-rean-d_202012",  # noqa: E501 Horizontal velocity (3d) - daily mean
    "med-cmcc-cur-rean-h_202012",  # noqa: E501 Horizontal surface velocity (2d) - hourly mean
    "med-cmcc-cur-rean-m_202012",  # noqa: E501 Horizontal velocity (3d) - monthly mean
    "med-cmcc-mld-int-m_202112",  # noqa: E501 Mixed layer depth (2d) - monthly mean
    "med-cmcc-mld-rean-d_202012",  # noqa: E501 Mixed layer depth (2d) - daily mean
    "med-cmcc-mld-rean-m_202012",  # noqa: E501 Mixed layer depth (2d) - monthly mean
    "med-cmcc-sal-int-m_202112",  # noqa: E501 Salinity (3d) - monthly mean
    "med-cmcc-sal-rean-d_202012",  # noqa: E501 Salinity (3d) - daily mean
    "med-cmcc-sal-rean-m_202012",  # noqa: E501 Salinity (3d) - monthly mean
    "med-cmcc-ssh-int-m_202112",  # noqa: E501 Sea surface height (2d) - monthly mean
    "med-cmcc-ssh-rean-d_202012",  # noqa: E501 Sea surface height (2d) - daily mean
    "med-cmcc-ssh-rean-h_202012",  # noqa: E501 Sea surface height (2d) - hourly mean
    "med-cmcc-ssh-rean-m_202012",  # noqa: E501 Sea surface height (2d) - monthly mean
    "med-cmcc-tem-int-m_202112",  # noqa: E501 Potential temperature (3d) - monthly mean
    "med-cmcc-tem-rean-d_202012",  # noqa: E501 Potential temperature (3d) - daily mean
    "med-cmcc-tem-rean-m_202012",  # noqa: E501 Potential temperature (3d) - monthly mean
]


class medsea_multiyear_phy(Main):
    name = "EO:MO:DAT:MEDSEA_MULTIYEAR_PHY_006_004"
    dataset = "EO:MO:DAT:MEDSEA_MULTIYEAR_PHY_006_004"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "bottomT",
            "bottomT_avg",
            "bottomT_std",
            "climatology_bnds",
            "depth",
            "lat",
            "lon",
            "mlotst",
            "mlotst_avg",
            "mlotst_std",
            "so",
            "so_avg",
            "so_std",
            "thetao",
            "thetao_avg",
            "thetao_std",
            "time",
            "uo",
            "uo_avg",
            "uo_std",
            "vo",
            "vo_avg",
            "vo_std",
            "zos",
            "zos_avg",
            "zos_std",
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
        if layer == "cmems_mod_med_phy-ssh_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-tem-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-cur-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-cur-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-tem-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy_my_4.2km-climatology_P1M-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-mld-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-tem-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-cur-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-sal-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-sal-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-cur-rean-h_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-mld-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-sal-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-mld_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-mld-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-cur_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-tem_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-rean-h_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-sal_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
