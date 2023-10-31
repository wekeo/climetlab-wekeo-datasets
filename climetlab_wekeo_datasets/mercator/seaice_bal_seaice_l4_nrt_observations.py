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
    "cmems_obs-si_bal_phy-sie_nrt_l4_P1D-m_202211",  # noqa: E501 cmems_obs-si_bal_phy-sie_nrt_l4_P1D-m_202211
    "FMI-BAL-SEAICE_CONC-L4-NRT-OBS",  # noqa: E501 Baltic ice concentration, l4, 1km daily (fmi-bal-seaice conc-l4-nrt-obs)
    "FMI-BAL-SEAICE_THICK-L4-NRT-OBS",  # noqa: E501 Baltic ice thickness, l4, 1km daily (fmi-bal-seaice thick-l4-nrt-obs)
]


class seaice_bal_seaice_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SEAICE_BAL_SEAICE_L4_NRT_OBSERVATIONS_011_004"
    dataset = "EO:MO:DAT:SEAICE_BAL_SEAICE_L4_NRT_OBSERVATIONS_011_004"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "concentration_range",
            "crs",
            "ice_concentration",
            "ice_thickness",
            "lat",
            "lon",
            "product_quality",
            "sea_ice_extent",
            "thickness_range",
            "time",
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
        if layer == "FMI-BAL-SEAICE_CONC-L4-NRT-OBS":
            if start is None:
                start = "2018-01-01T14:00:00Z"

            if end is None:
                end = "2023-05-28T13:00:00Z"

        if layer == "FMI-BAL-SEAICE_THICK-L4-NRT-OBS":
            if start is None:
                start = "2018-01-01T14:00:00Z"

            if end is None:
                end = "2023-05-28T13:00:00Z"

        if layer == "cmems_obs-si_bal_phy-sie_nrt_l4_P1D-m_202211":
            if start is None:
                start = "2022-11-21T14:00:00Z"

            if end is None:
                end = "2023-05-28T14:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
