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


class satellite_earth_radiation_budget(Main):
    name = "EO:ECMWF:DAT:SATELLITE_EARTH_RADIATION_BUDGET"
    dataset = "EO:ECMWF:DAT:SATELLITE_EARTH_RADIATION_BUDGET"

    choices = [
        "origin",
        "format_",
    ]

    string_selects = [
        "month",
        "sensor",
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
        "sensor",
        [
            "aatsr",
            "atsr2",
            "slstr_on_sentinel_3a",
            "slstr_on_sentinel_3b",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "all_available_variables",
            "incoming_shortwave_radiation",
            "outgoing_longwave_radiation",
            "outgoing_shortwave_radiation",
            "total_solar_irradiance",
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
        ],
        multiple=True,
    )
    @normalize("area", "bounding-box(list)")
    @normalize(
        "origin",
        [
            "c3s_cci",
            "c3s_rmib",
            "esa_cloud_cci",
            "nasa_ceres_ebaf",
            "noaa_ncei_hirs",
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
        month,
        sensor,
        variable,
        year,
        area=None,
        origin=None,
        format_=None,
    ):
        super().__init__(
            month=month,
            sensor=sensor,
            variable=variable,
            year=year,
            area=area,
            origin=origin,
            format_=format_,
        )
