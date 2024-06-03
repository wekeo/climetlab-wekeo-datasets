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
    "cmems_mod_med_phy-cur_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_phy-cur_my_4.2km_P1Y-m
    "cmems_mod_med_phy-mld_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_phy-mld_my_4.2km_P1Y-m
    "cmems_mod_med_phy-sal_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_phy-sal_my_4.2km_P1Y-m
    "cmems_mod_med_phy-ssh_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_phy-ssh_my_4.2km_P1Y-m
    "cmems_mod_med_phy-tem_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_phy-tem_my_4.2km_P1Y-m
    "cmems_mod_med_phy_my_4.2km_static_202211",  # noqa: E501 cmems_mod_med_phy_my_4.2km_static
    "med-cmcc-cur-int-m_202112",  # noqa: E501 med-cmcc-cur-int-m
    "med-cmcc-cur-rean-d_202012",  # noqa: E501 med-cmcc-cur-rean-d
    "med-cmcc-cur-rean-m_202012",  # noqa: E501 med-cmcc-cur-rean-m
    "med-cmcc-mld-int-m_202112",  # noqa: E501 med-cmcc-mld-int-m
    "med-cmcc-mld-rean-d_202012",  # noqa: E501 med-cmcc-mld-rean-d
    "med-cmcc-mld-rean-m_202012",  # noqa: E501 med-cmcc-mld-rean-m
    "med-cmcc-sal-int-m_202112",  # noqa: E501 med-cmcc-sal-int-m
    "med-cmcc-sal-rean-d_202012",  # noqa: E501 med-cmcc-sal-rean-d
    "med-cmcc-sal-rean-m_202012",  # noqa: E501 med-cmcc-sal-rean-m
    "med-cmcc-ssh-int-m_202112",  # noqa: E501 med-cmcc-ssh-int-m
    "med-cmcc-ssh-rean-d_202012",  # noqa: E501 med-cmcc-ssh-rean-d
    "med-cmcc-ssh-rean-m_202012",  # noqa: E501 med-cmcc-ssh-rean-m
    "med-cmcc-tem-int-m_202112",  # noqa: E501 med-cmcc-tem-int-m
    "med-cmcc-tem-rean-d_202012",  # noqa: E501 med-cmcc-tem-rean-d
    "med-cmcc-tem-rean-m_202012",  # noqa: E501 med-cmcc-tem-rean-m
]


class medsea_multiyear_phy(Main):
    name = "EO:MO:DAT:MEDSEA_MULTIYEAR_PHY_006_004"
    dataset = "EO:MO:DAT:MEDSEA_MULTIYEAR_PHY_006_004"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "deptho",
            "deptho_lev",
            "lat",
            "latitude",
            "lon",
            "longitude",
            "mask",
            "mlotst",
            "so",
            "thetao",
            "time",
            "uo",
            "vo",
            "zos",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-04-16T12:00:00Z",
        min_date="2021-07-16T12:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_med_phy-cur_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1987-07-01T17:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-mld_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1987-07-01T17:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-sal_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1987-07-01T17:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1987-07-01T17:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-tem_my_4.2km_P1Y-m_202211":
            if min_date is None:
                min_date = "1987-07-01T17:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy_my_4.2km_static_202211":
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-28T00:00:00Z"

        if layer == "med-cmcc-cur-int-m_202112":
            if min_date is None:
                min_date = "2021-07-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T12:00:00Z"

        if layer == "med-cmcc-cur-rean-d_202012":
            if min_date is None:
                min_date = "1987-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-cur-rean-m_202012":
            if min_date is None:
                min_date = "1987-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-mld-int-m_202112":
            if min_date is None:
                min_date = "2021-07-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T12:00:00Z"

        if layer == "med-cmcc-mld-rean-d_202012":
            if min_date is None:
                min_date = "1987-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-mld-rean-m_202012":
            if min_date is None:
                min_date = "1987-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-sal-int-m_202112":
            if min_date is None:
                min_date = "2021-07-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T12:00:00Z"

        if layer == "med-cmcc-sal-rean-d_202012":
            if min_date is None:
                min_date = "1987-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-sal-rean-m_202012":
            if min_date is None:
                min_date = "1987-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-int-m_202112":
            if min_date is None:
                min_date = "2021-07-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T12:00:00Z"

        if layer == "med-cmcc-ssh-rean-d_202012":
            if min_date is None:
                min_date = "1987-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-rean-m_202012":
            if min_date is None:
                min_date = "1987-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-tem-int-m_202112":
            if min_date is None:
                min_date = "2021-07-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T12:00:00Z"

        if layer == "med-cmcc-tem-rean-d_202012":
            if min_date is None:
                min_date = "1987-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-tem-rean-m_202012":
            if min_date is None:
                min_date = "1987-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2022-09-01T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
