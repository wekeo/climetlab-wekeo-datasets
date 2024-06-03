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


class sis_shipping_consumption_on_routes(Main):
    name = "EO:ECMWF:DAT:SIS_SHIPPING_CONSUMPTION_ON_ROUTES"
    dataset = "EO:ECMWF:DAT:SIS_SHIPPING_CONSUMPTION_ON_ROUTES"

    @normalize(
        "arrival_port",
        [
            "bimini_island",
            "bishop_rock",
            "bombay",
            "cape_of_good_hope",
            "cook_strait",
            "gibraltar",
            "luzon",
            "new_york",
            "panama",
            "san_francisco",
            "sydney",
            "valparaiso",
            "yokohama",
        ],
    )
    @normalize(
        "departure_port",
        [
            "bimini_island",
            "bishop_rock",
            "bombay",
            "cape_of_good_hope",
            "cook_strait",
            "gibraltar",
            "luzon",
            "new_york",
            "panama",
            "san_francisco",
            "sydney",
            "valparaiso",
            "yokohama",
        ],
    )
    @normalize(
        "forecast_start_month",
        [
            "february",
            "january",
            "march",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "climatology",
            "historical",
            "seasonal_forecast",
        ],
    )
    @normalize(
        "statistic",
        [
            "daily",
            "monthly_10th_percentile",
            "monthly_25th_percentile",
            "monthly_5th_percentile",
            "monthly_75th_percentile",
            "monthly_90th_percentile",
            "monthly_95th_percentile",
            "monthly_average",
            "seasonal_forecast_ensemble_average",
            "seasonal_forecast_monthly_average",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "fuel_consumption_at_fixed_shaft_power",
            "fuel_consumption_at_fixed_speed",
            "shaft_power_at_fixed_speed",
            "ship_speed_at_fixed_shaft_power",
            "trip_duration_at_fixed_shaft_power",
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
            "2019",
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
    def __init__(
        self,
        arrival_port,
        departure_port,
        forecast_start_month,
        product_type,
        statistic,
        variable,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            arrival_port=arrival_port,
            departure_port=departure_port,
            forecast_start_month=forecast_start_month,
            product_type=product_type,
            statistic=statistic,
            variable=variable,
            year=year,
            format_=format_,
            limit=limit,
        )
