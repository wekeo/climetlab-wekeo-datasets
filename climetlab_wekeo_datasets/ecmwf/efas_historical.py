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


class efas_historical(Main):
    name = "EO:ECMWF:DAT:EFAS_HISTORICAL"
    dataset = "EO:ECMWF:DAT:EFAS_HISTORICAL"

    @normalize(
        "system_version",
        [
            "version_2_0",
            "version_3_0",
            "version_3_5",
            "version_4_0",
            "version_5_0",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "elevation",
            "field_capacity",
            "river_discharge_in_the_last_24_hours",
            "river_discharge_in_the_last_6_hours",
            "runoff_water_equivalent",
            "snow_depth_water_equivalent",
            "soil_depth",
            "soil_wetness_index",
            "upstream_area",
            "volumetric_soil_moisture",
            "wilting_point",
        ],
    )
    @normalize(
        "model_levels",
        [
            "soil_levels",
            "surface_level",
        ],
    )
    @normalize(
        "soil_level",
        [
            "1",
            "2",
            "3",
        ],
        multiple=True,
    )
    @normalize(
        "hyear",
        [
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
        "hmonth",
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
        "hday",
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
        "time",
        [
            "00:00",
            "06:00",
            "12:00",
            "18:00",
        ],
        multiple=True,
    )
    @normalize(
        "format_",
        [
            "grib.zip",
            "netcdf4.zip",
        ],
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(
        self,
        system_version,
        variable,
        model_levels,
        soil_level,
        hyear,
        hmonth,
        hday,
        time,
        format_=None,
        bbox=None,
        limit=None,
    ):
        super().__init__(
            system_version=system_version,
            variable=variable,
            model_levels=model_levels,
            soil_level=soil_level,
            hyear=hyear,
            hmonth=hmonth,
            hday=hday,
            time=time,
            format_=format_,
            bbox=bbox,
            limit=limit,
        )
