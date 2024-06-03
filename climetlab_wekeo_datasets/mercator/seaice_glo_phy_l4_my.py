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
    "cmems_obs-si_glo_phy-drift-north_my_l4_P1D-m_202311",  # noqa: E501 cmems_obs-si_glo_phy-drift-north_my_l4_P1D-m_202311
    "cmems_obs-si_glo_phy-drift-south_my_l4_P1D-m_202311",  # noqa: E501 cmems_obs-si_glo_phy-drift-south_my_l4_P1D-m_202311
]


class seaice_glo_phy_l4_my(Main):
    name = "EO:MO:DAT:SEAICE_GLO_PHY_L4_MY_011_020"
    dataset = "EO:MO:DAT:SEAICE_GLO_PHY_L4_MY_011_020"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "Polar_Stereographic_Grid",
            "dXY_count",
            "dX_mean",
            "dX_std",
            "dY_mean",
            "dY_std",
            "divergence",
            "lat",
            "lon",
            "qos_bnds_from_time",
            "qos_bnds_to_time",
            "qos_mean_dX",
            "qos_mean_dY",
            "qos_sample_count",
            "qos_stddev_dX",
            "qos_stddev_dY",
            "shear",
            "status_flag",
            "time",
            "time_first",
            "time_last",
            "time_period_end",
            "time_period_start",
            "vorticity",
            "xc",
            "yc",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2023-10-02T00:00:00Z",
        min_date="2014-10-05T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-si_glo_phy-drift-north_my_l4_P1D-m_202311":
            if min_date is None:
                min_date = "2014-10-05T00:00:00Z"

            if max_date is None:
                max_date = "2023-10-02T00:00:00Z"

        if layer == "cmems_obs-si_glo_phy-drift-south_my_l4_P1D-m_202311":
            if min_date is None:
                min_date = "2014-10-05T00:00:00Z"

            if max_date is None:
                max_date = "2023-10-02T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
