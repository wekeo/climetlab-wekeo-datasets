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


class sis_energy_derived_reanalysis(Main):
    name = "EO:ECMWF:DAT:SIS_ENERGY_DERIVED_REANALYSIS"
    dataset = "EO:ECMWF:DAT:SIS_ENERGY_DERIVED_REANALYSIS"

    @normalize(
        "energy_product_type",
        [
            "capacity_factor_ratio",
            "energy",
            "power",
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
        "spatial_aggregation",
        [
            "country_level",
            "maritime_country_level",
            "maritime_sub_country_level",
            "original_grid",
            "sub_country_level",
        ],
        multiple=True,
    )
    @normalize(
        "temporal_aggregation",
        [
            "annual",
            "daily",
            "hourly",
            "monthly",
            "seasonal",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "2m_air_temperature",
            "electricity_demand",
            "hydro_power_generation_reservoirs",
            "hydro_power_generation_rivers",
            "pressure_at_sea_level",
            "solar_photovoltaic_power_generation",
            "surface_downwelling_shortwave_radiation",
            "total_precipitation",
            "wind_power_generation_offshore",
            "wind_power_generation_onshore",
            "wind_speed_at_100m",
            "wind_speed_at_10m",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1979",
            "1980",
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
            "2024",
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
        energy_product_type,
        month,
        spatial_aggregation,
        temporal_aggregation,
        variable,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            energy_product_type=energy_product_type,
            month=month,
            spatial_aggregation=spatial_aggregation,
            temporal_aggregation=temporal_aggregation,
            variable=variable,
            year=year,
            format_=format_,
            limit=limit,
        )
