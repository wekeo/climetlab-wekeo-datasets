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


class cams_global_ghg_reanalysis_egg4_monthly(Main):
    name = "EO:ECMWF:DAT:CAMS_GLOBAL_GHG_REANALYSIS_EGG4_MONTHLY"
    dataset = "EO:ECMWF:DAT:CAMS_GLOBAL_GHG_REANALYSIS_EGG4_MONTHLY"

    choices = [
        "format_",
    ]

    string_selects = [
        "month",
        "pressure_level",
        "product_type",
        "step",
        "time",
        "variable",
        "year",
    ]

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
            "monthly_mean",
            "monthly_mean_by_hour_of_day",
        ],
        multiple=True,
    )
    @normalize(
        "step",
        [
            "12",
            "15",
            "18",
            "21",
            "24",
            "3",
            "6",
            "9",
        ],
        multiple=True,
    )
    @normalize(
        "time",
        [
            "00:00",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "2m_dewpoint_temperature",
            "2m_temperature",
            "accumulated_carbon_dioxide_ecosystem_respiration",
            "accumulated_carbon_dioxide_gross_primary_production",
            "accumulated_carbon_dioxide_net_ecosystem_exchange",
            "carbon_dioxide",
            "ch4_column_mean_molar_fraction",
            "co2_column_mean_molar_fraction",
            "flux_of_carbon_dioxide_ecosystem_respiration",
            "flux_of_carbon_dioxide_gross_primary_production",
            "flux_of_carbon_dioxide_net_ecosystem_exchange",
            "geopotential",
            "mean_sea_level_pressure",
            "methane",
            "relative_humidity",
            "sea_ice_cover",
            "sea_surface_temperature",
            "snow_albedo",
            "snow_depth",
            "temperature",
            "total_column_water",
            "total_column_water_vapour",
            "vertical_velocity",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    @normalize("area", "bounding-box(list)")
    @normalize(
        "pressure_level",
        [
            "1",
            "10",
            "100",
            "1000",
            "150",
            "2",
            "20",
            "200",
            "250",
            "3",
            "30",
            "300",
            "400",
            "5",
            "50",
            "500",
            "600",
            "7",
            "70",
            "700",
            "800",
            "850",
            "900",
            "925",
            "950",
        ],
        multiple=True,
    )
    def __init__(
        self,
        month,
        product_type,
        step,
        time,
        variable,
        year,
        format_,
        area=None,
        pressure_level=None,
    ):
        super().__init__(
            month=month,
            product_type=product_type,
            step=step,
            time=time,
            variable=variable,
            year=year,
            format_=format_,
            area=area,
            pressure_level=pressure_level,
        )
