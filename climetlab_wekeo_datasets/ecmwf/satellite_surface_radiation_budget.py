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


class satellite_surface_radiation_budget(Main):
    name = "EO:ECMWF:DAT:SATELLITE_SURFACE_RADIATION_BUDGET"
    dataset = "EO:ECMWF:DAT:SATELLITE_SURFACE_RADIATION_BUDGET"

    choices = [
        "product_family",
        "origin",
        "climate_data_record_type",
        "time_aggregation",
        "version",
        "format_",
    ]

    string_selects = [
        "day",
        "month",
        "sensor_on_satellite",
        "variable",
        "year",
    ]

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
        "sensor_on_satellite",
        [
            "aatsr_on_envisat",
            "atsr2_on_ers2",
            "avhrr_on_multiple_satellites",
            "slstr_on_sentinel_3a_is_under_investigation",
            "slstr_on_sentinel_3b_is_under_investigation",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "all_variables",
            "surface_downwelling_longwave_flux",
            "surface_downwelling_shortwave_flux",
            "surface_net_downward_longwave_flux",
            "surface_net_downward_radiative_flux",
            "surface_net_downward_shortwave_flux",
            "surface_upwelling_longwave_flux",
            "surface_upwelling_shortwave_flux",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "product_family",
        [
            "cci",
            "clara",
        ],
    )
    @normalize(
        "origin",
        [
            "c3s",
            "esa",
            "eumetsat",
        ],
    )
    @normalize(
        "climate_data_record_type",
        [
            "interim_climate_data_record",
            "thematic_climate_data_record",
        ],
    )
    @normalize(
        "time_aggregation",
        [
            "daily_mean",
            "monthly_mean",
        ],
    )
    @normalize(
        "version",
        [
            "v2_0",
            "v2_0_1",
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
        day,
        month,
        sensor_on_satellite,
        variable,
        year,
        product_family=None,
        origin=None,
        climate_data_record_type=None,
        time_aggregation=None,
        version=None,
        format_=None,
    ):
        super().__init__(
            day=day,
            month=month,
            sensor_on_satellite=sensor_on_satellite,
            variable=variable,
            year=year,
            product_family=product_family,
            origin=origin,
            climate_data_record_type=climate_data_record_type,
            time_aggregation=time_aggregation,
            version=version,
            format_=format_,
        )
