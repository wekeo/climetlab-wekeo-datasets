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


class satellite_total_column_water_vapour_land_ocean(Main):
    name = "EO:ECMWF:DAT:SATELLITE_TOTAL_COLUMN_WATER_VAPOUR_LAND_OCEAN"
    dataset = "EO:ECMWF:DAT:SATELLITE_TOTAL_COLUMN_WATER_VAPOUR_LAND_OCEAN"

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
        "horizontal_aggregation",
        [
            "0_05_x_0_05",
            "0_5_x_0_5",
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
        "product",
        [
            "c3s_meris_and_ssm_i",
            "near_infrared_hoaps_combined",
        ],
    )
    @normalize(
        "temporal_aggregation",
        [
            "daily",
            "monthly",
        ],
    )
    @normalize(
        "year",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "all",
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
        horizontal_aggregation,
        month,
        product,
        temporal_aggregation,
        year,
        variable="all",
        format_=None,
        limit=None,
    ):
        super().__init__(
            day=day,
            horizontal_aggregation=horizontal_aggregation,
            month=month,
            product=product,
            temporal_aggregation=temporal_aggregation,
            year=year,
            variable=variable,
            format_=format_,
            limit=limit,
        )
