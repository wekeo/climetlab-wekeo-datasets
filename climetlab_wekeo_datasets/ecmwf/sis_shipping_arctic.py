#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.ecmwf.main import Main


class sis_shipping_arctic(Main):
    name = "EO:ECMWF:DAT:SIS_SHIPPING_ARCTIC"
    dataset = "EO:ECMWF:DAT:SIS_SHIPPING_ARCTIC"

    @normalize(
        "experiment",
        [
            "RCP4.5",
            "RCP8.5",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "ensemble_mean",
            "ensemble_mean_minus_ensemble_standard_deviation",
            "ensemble_mean_plus_ensemble_standard_deviation",
        ],
    )
    @normalize(
        "variable",
        [
            "arctic_accessibility_index_map_arc4",
            "arctic_accessibility_index_map_arc5",
            "arctic_accessibility_index_map_arc6",
            "arctic_accessibility_index_map_arc7",
            "arctic_accessibility_index_map_arc8",
            "arctic_accessibility_index_map_arc9",
            "fuel_consumption",
            "ice_resistance",
            "icebreaker_need",
            "maximum_sea_ice_extent_map",
            "mean_sea_ice_concentration_map",
            "mean_sea_ice_extent_map",
            "minimum_sea_ice_extent_map",
            "overall_cost_of_the_arctic_route_crossing",
            "sea_ice_thickness_map",
            "shaft_power",
            "ship_speed",
            "trip_duration",
        ],
        multiple=True,
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(self, experiment, product_type, variable, format_=None, limit=None):
        super().__init__(
            experiment=experiment,
            product_type=product_type,
            variable=variable,
            format_=format_,
            limit=limit,
        )
