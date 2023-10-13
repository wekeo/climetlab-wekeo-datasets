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


class seasonal_postprocessed_single_levels(Main):
    name = "EO:ECMWF:DAT:SEASONAL_POSTPROCESSED_SINGLE_LEVELS"
    dataset = "EO:ECMWF:DAT:SEASONAL_POSTPROCESSED_SINGLE_LEVELS"

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
            "monthly_mean",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "10m_u_component_of_wind_anomaly",
            "10m_v_component_of_wind_anomaly",
            "10m_wind_gust_anomaly",
            "10m_wind_speed_anomaly",
            "2m_dewpoint_temperature_anomaly",
            "2m_temperature_anomaly",
            "east_west_surface_stress_anomalous_rate_of_accumulation",
            "evaporation_anomalous_rate_of_accumulation",
            "maximum_2m_temperature_in_the_last_24_hours_anomaly",
            "mean_sea_level_pressure_anomaly",
            "mean_sub_surface_runoff_rate_anomaly",
            "mean_surface_runoff_rate_anomaly",
            "minimum_2m_temperature_in_the_last_24_hours_anomaly",
            "north_south_surface_stress_anomalous_rate_of_accumulation",
            "runoff_anomalous_rate_of_accumulation",
            "sea_ice_cover_anomaly",
            "sea_surface_temperature_anomaly",
            "snow_density_anomaly",
            "snow_depth_anomaly",
            "snowfall_anomalous_rate_of_accumulation",
            "soil_temperature_anomaly_level_1",
            "solar_insolation_anomalous_rate_of_accumulation",
            "surface_latent_heat_flux_anomalous_rate_of_accumulation",
            "surface_sensible_heat_flux_anomalous_rate_of_accumulation",
            "surface_solar_radiation_anomalous_rate_of_accumulation",
            "surface_solar_radiation_downwards_anomalous_rate_of_accumulation",
            "surface_thermal_radiation_anomalous_rate_of_accumulation",
            "surface_thermal_radiation_downwards_anomalous_rate_of_accumulation",
            "top_solar_radiation_anomalous_rate_of_accumulation",
            "top_thermal_radiation_anomalous_rate_of_accumulation",
            "total_cloud_cover_anomaly",
            "total_column_cloud_ice_water_anomaly",
            "total_column_cloud_liquid_water_anomaly",
            "total_column_water_vapour_anomaly",
            "total_precipitation_anomalous_rate_of_accumulation",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
