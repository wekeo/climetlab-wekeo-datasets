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


class seasonal_monthly_ocean(Main):
    name = "EO:ECMWF:DAT:SEASONAL_MONTHLY_OCEAN"
    dataset = "EO:ECMWF:DAT:SEASONAL_MONTHLY_OCEAN"

    choices = [
        "originating_centre",
        "system",
        "format_",
    ]

    string_selects = [
        "forecast_type",
        "month",
        "variable",
        "year",
    ]

    @normalize(
        "forecast_type",
        [
            "forecast",
            "hindcast",
        ],
        multiple=True,
    )
    @normalize(
        "month",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "depth_average_potential_temperature_of_upper_300m",
            "depth_average_salinity_of_upper_300m",
            "depth_of_14_c_isotherm",
            "depth_of_17_c_isotherm",
            "depth_of_20_c_isotherm",
            "depth_of_26_c_isotherm",
            "depth_of_28_c_isotherm",
            "mixed_layer_depth_0_01",
            "mixed_layer_depth_0_03",
            "sea_ice_thickness",
            "sea_surface_height_above_geoid",
            "sea_surface_salinity",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "2000",
            "2001",
            "2002",
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
            "2019",
            "2023",
        ],
        multiple=True,
    )
    @normalize(
        "originating_centre",
        [
            "cmcc",
            "dwd",
            "ecmwf",
            "meteo_france",
            "ukmo",
        ],
    )
    @normalize(
        "system",
        [
            "21",
            "35",
            "51",
            "602",
            "8",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        forecast_type,
        month,
        variable,
        year,
        originating_centre,
        system,
        format_,
    ):
        super().__init__(
            forecast_type=forecast_type,
            month=month,
            variable=variable,
            year=year,
            originating_centre=originating_centre,
            system=system,
            format_=format_,
        )
