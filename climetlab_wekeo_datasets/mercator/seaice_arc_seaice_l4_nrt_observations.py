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
    "cmems_obs-si_arc_physic_nrt_1km-grl_P1D-irr_202012",  # noqa: E501 Arctic sea ice greenland
    "cmems_obs-si_arc_physic_nrt_1km-grl_P1WT3D-m_202012",  # noqa: E501 Arctic sea ice greenland overview
    "METNO-ARC-SEAICE_CONC-L4-NRT-OBS",  # noqa: E501 Arctic sea ice svalbard
]


class seaice_arc_seaice_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SEAICE_ARC_SEAICE_L4_NRT_OBSERVATIONS_011_002"
    dataset = "EO:MO:DAT:SEAICE_ARC_SEAICE_L4_NRT_OBSERVATIONS_011_002"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "CA",
            "CB",
            "CC",
            "CD",
            "CF",
            "CN",
            "CT",
            "FA",
            "FB",
            "FC",
            "POLY_TYPE",
            "SA",
            "SB",
            "SC",
            "concentration_range",
            "crs",
            "ice_concentration",
            "ice_poly_id_grid",
            "lat",
            "lon",
            "polygon_id",
            "polygon_reference",
            "time",
            "xc",
            "yc",
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
        if layer == "METNO-ARC-SEAICE_CONC-L4-NRT-OBS":
            if start is None:
                start = "2023-03-20T00:00:00Z"

            if end is None:
                end = "2023-03-20T00:00:00Z"

        if layer == "cmems_obs-si_arc_physic_nrt_1km-grl_P1D-irr_202012":
            if start is None:
                start = "0090-11-21T00:00:00Z"

            if end is None:
                end = "3012-12-03T00:00:00Z"

        if layer == "cmems_obs-si_arc_physic_nrt_1km-grl_P1WT3D-m_202012":
            if start is None:
                start = "0092-01-20T00:00:00Z"

            if end is None:
                end = "3011-11-20T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
