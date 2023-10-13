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


class reanalysis_era5_pressure_levels_monthly_means_preliminary_back_extension(Main):
    name = "EO:ECMWF:DAT:REANALYSIS_ERA5_PRESSURE_LEVELS_MONTHLY_MEANS_PRELIMINARY_BACK_EXTENSION"
    dataset = "EO:ECMWF:DAT:REANALYSIS_ERA5_PRESSURE_LEVELS_MONTHLY_MEANS_PRELIMINARY_BACK_EXTENSION"

    choices = [
        "format_",
    ]

    string_selects = [
        "time",
        "product_type",
        "variable",
        "year",
        "pressure_level",
        "month",
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
        "pressure_level",
        [
            "1",
            "10",
            "100",
            "1000",
            "125",
            "150",
            "175",
            "2",
            "20",
            "200",
            "225",
            "250",
            "3",
            "30",
            "300",
            "350",
            "400",
            "450",
            "5",
            "50",
            "500",
            "550",
            "600",
            "650",
            "7",
            "70",
            "700",
            "750",
            "775",
            "800",
            "825",
            "850",
            "875",
            "900",
            "925",
            "950",
            "975",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "members-monthly-means-of-daily-means",
            "members-synoptic-monthly-means",
            "reanalysis-monthly-means-of-daily-means",
            "reanalysis-synoptic-monthly-means",
        ],
        multiple=True,
    )
    @normalize(
        "time",
        [
            "00:00",
            "01:00",
            "02:00",
            "03:00",
            "04:00",
            "05:00",
            "06:00",
            "07:00",
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "divergence",
            "fraction_of_cloud_cover",
            "geopotential",
            "ozone_mass_mixing_ratio",
            "potential_vorticity",
            "relative_humidity",
            "specific_cloud_ice_water_content",
            "specific_cloud_liquid_water_content",
            "specific_humidity",
            "specific_rain_water_content",
            "specific_snow_water_content",
            "temperature",
            "u_component_of_wind",
            "v_component_of_wind",
            "vertical_velocity",
            "vorticity",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1950",
            "1951",
            "1952",
            "1953",
            "1954",
            "1955",
            "1956",
            "1957",
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
    def __init__(
        self,
        month,
        pressure_level,
        product_type,
        time,
        variable,
        year,
        format_,
        area=None,
    ):
        super().__init__(
            month=month,
            pressure_level=pressure_level,
            product_type=product_type,
            time=time,
            variable=variable,
            year=year,
            format_=format_,
            area=area,
        )
