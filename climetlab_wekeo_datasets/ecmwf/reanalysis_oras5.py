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


class reanalysis_oras5(Main):
    name = "EO:ECMWF:DAT:REANALYSIS_ORAS5"
    dataset = "EO:ECMWF:DAT:REANALYSIS_ORAS5"

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
            "consolidated",
            "operational",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "depth_of_14_c_isotherm",
            "depth_of_17_c_isotherm",
            "depth_of_20_c_isotherm",
            "depth_of_26_c_isotherm",
            "depth_of_28_c_isotherm",
            "meridional_velocity",
            "meridional_wind_stress",
            "mixed_layer_depth_0_01",
            "mixed_layer_depth_0_03",
            "net_downward_heat_flux",
            "net_upward_water_flux",
            "ocean_heat_content_for_the_total_water_column",
            "ocean_heat_content_for_the_upper_300m",
            "ocean_heat_content_for_the_upper_700m",
            "potential_temperature",
            "rotated_meridional_velocity",
            "rotated_zonal_velocity",
            "salinity",
            "sea_ice_concentration",
            "sea_ice_meridional_velocity",
            "sea_ice_thickness",
            "sea_ice_zonal_velocity",
            "sea_surface_height",
            "sea_surface_salinity",
            "sea_surface_temperature",
            "zonal_velocity",
            "zonal_wind_stress",
        ],
        multiple=True,
    )
    @normalize(
        "vertical_resolution",
        [
            "all_levels",
            "single_level",
        ],
    )
    @normalize(
        "year",
        [
            "1958",
            "1959",
            "1960",
            "1961",
            "1962",
            "1963",
            "1964",
            "1965",
            "1966",
            "1967",
            "1968",
            "1969",
            "1970",
            "1971",
            "1972",
            "1973",
            "1974",
            "1975",
            "1976",
            "1977",
            "1978",
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
        month,
        product_type,
        variable,
        vertical_resolution,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            month=month,
            product_type=product_type,
            variable=variable,
            vertical_resolution=vertical_resolution,
            year=year,
            format_=format_,
            limit=limit,
        )
