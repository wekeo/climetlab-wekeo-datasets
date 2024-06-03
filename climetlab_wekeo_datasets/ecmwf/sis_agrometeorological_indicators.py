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


class sis_agrometeorological_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_AGROMETEOROLOGICAL_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_AGROMETEOROLOGICAL_INDICATORS"

    @normalize(
        "day",
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
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
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
        "statistic",
        [
            "24_hour_maximum",
            "24_hour_mean",
            "24_hour_minimum",
            "day_time_maximum",
            "day_time_mean",
            "night_time_mean",
            "night_time_minimum",
        ],
        multiple=True,
    )
    @normalize(
        "time",
        [
            "06_00",
            "09_00",
            "12_00",
            "15_00",
            "18_00",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "10m_wind_speed",
            "2m_dewpoint_temperature",
            "2m_relative_humidity",
            "2m_temperature",
            "cloud_cover",
            "liquid_precipitation_duration_fraction",
            "precipitation_flux",
            "snow_thickness",
            "snow_thickness_lwe",
            "solar_radiation_flux",
            "solid_precipitation_duration_fraction",
            "vapour_pressure",
        ],
    )
    @normalize(
        "version",
        [
            "1_0",
            "1_1",
        ],
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
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        day,
        month,
        statistic,
        time,
        variable,
        version,
        year,
        bbox=None,
        format_=None,
        limit=None,
    ):
        super().__init__(
            day=day,
            month=month,
            statistic=statistic,
            time=time,
            variable=variable,
            version=version,
            year=year,
            bbox=bbox,
            format_=format_,
            limit=limit,
        )
