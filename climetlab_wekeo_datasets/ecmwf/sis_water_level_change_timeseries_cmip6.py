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


class sis_water_level_change_timeseries_cmip6(Main):
    name = "EO:ECMWF:DAT:SIS_WATER_LEVEL_CHANGE_TIMESERIES_CMIP6"
    dataset = "EO:ECMWF:DAT:SIS_WATER_LEVEL_CHANGE_TIMESERIES_CMIP6"

    @normalize(
        "experiment",
        [
            "future",
            "historical",
            "reanalysis",
        ],
    )
    @normalize(
        "model",
        [
            "CMCC-CM2-VHR4",
            "EC-Earth3P-HR",
            "GFDL-CM4C192-SST",
            "HadGEM3-GC31-HM",
            "HadGEM3-GC31-HM-SST",
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
        "temporal_aggregation",
        [
            "10_min",
            "annual",
            "daily_maximum",
            "hourly",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "mean_sea_level",
            "storm_surge_residual",
            "tidal_elevation",
            "total_water_level",
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
            "2025",
            "2026",
            "2027",
            "2028",
            "2029",
            "2030",
            "2031",
            "2032",
            "2033",
            "2034",
            "2035",
            "2036",
            "2037",
            "2038",
            "2039",
            "2040",
            "2041",
            "2042",
            "2043",
            "2044",
            "2045",
            "2046",
            "2047",
            "2048",
            "2049",
            "2050",
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
        experiment,
        model,
        month,
        temporal_aggregation,
        variable,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            experiment=experiment,
            model=model,
            month=month,
            temporal_aggregation=temporal_aggregation,
            variable=variable,
            year=year,
            format_=format_,
            limit=limit,
        )
