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


class seasonal_monthly_single_levels(Main):
    name = "EO:ECMWF:DAT:SEASONAL_MONTHLY_SINGLE_LEVELS"
    dataset = "EO:ECMWF:DAT:SEASONAL_MONTHLY_SINGLE_LEVELS"

    choices = [
        "originating_centre",
        "system",
        "format_",
    ]

    string_selects = [
        "leadtime_month",
        "month",
        "product_type",
        "variable",
        "year",
    ]

    @normalize(
        "leadtime_month",
        [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
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
        "product_type",
        [
            "ensemble_mean",
            "hindcast_climate_mean",
            "monthly_maximum",
            "monthly_mean",
            "monthly_minimum",
            "monthly_standard_deviation",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "10m_wind_gust_since_previous_post_processing",
            "10m_wind_speed",
            "2m_dewpoint_temperature",
            "2m_temperature",
            "east_west_surface_stress_rate_of_accumulation",
            "evaporation",
            "maximum_2m_temperature_in_the_last_24_hours",
            "mean_sea_level_pressure",
            "mean_sub_surface_runoff_rate",
            "mean_surface_runoff_rate",
            "minimum_2m_temperature_in_the_last_24_hours",
            "north_south_surface_stress_rate_of_accumulation",
            "runoff",
            "sea_ice_cover",
            "sea_surface_temperature",
            "snow_density",
            "snow_depth",
            "snowfall",
            "soil_temperature_level_1",
            "solar_insolation_rate_of_accumulation",
            "surface_latent_heat_flux",
            "surface_sensible_heat_flux",
            "surface_solar_radiation",
            "surface_solar_radiation_downwards",
            "surface_thermal_radiation",
            "surface_thermal_radiation_downwards",
            "top_solar_radiation",
            "top_thermal_radiation",
            "total_cloud_cover",
            "total_column_cloud_ice_water",
            "total_column_cloud_liquid_water",
            "total_column_water_vapour",
            "total_precipitation",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1981",
            "1982",
            "1983",
            "1984",
            "1985",
            "1986",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1992",
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
            "2020",
            "2021",
            "2022",
            "2023",
        ],
        multiple=True,
    )
    @normalize(
        "originating_centre",
        [
            "cmcc",
            "dwd",
            "eccc",
            "ecmwf",
            "jma",
            "meteo_france",
            "ncep",
            "ukmo",
        ],
    )
    @normalize(
        "system",
        [
            "1",
            "12",
            "13",
            "14",
            "15",
            "2",
            "21",
            "3",
            "35",
            "4",
            "5",
            "51",
            "6",
            "600",
            "601",
            "602",
            "7",
            "8",
        ],
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    @normalize("area", "bounding-box(list)")
    def __init__(
        self,
        leadtime_month,
        month,
        product_type,
        variable,
        year,
        originating_centre,
        system,
        format_,
        area=None,
    ):
        super().__init__(
            leadtime_month=leadtime_month,
            month=month,
            product_type=product_type,
            variable=variable,
            year=year,
            originating_centre=originating_centre,
            system=system,
            format_=format_,
            area=area,
        )
