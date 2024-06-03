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


class insitu_observations_gruan_reference_network(Main):
    name = "EO:ECMWF:DAT:INSITU_OBSERVATIONS_GRUAN_REFERENCE_NETWORK"
    dataset = "EO:ECMWF:DAT:INSITU_OBSERVATIONS_GRUAN_REFERENCE_NETWORK"

    @normalize("bbox", "bounding-box(list)")
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
        "format_",
        [
            "csv-lev.zip",
            "csv-obs.zip",
        ],
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
    )
    @normalize(
        "variable",
        [
            "air_temperature",
            "air_temperature_post_processing_radiation_correction",
            "air_temperature_random_uncertainty",
            "air_temperature_systematic_uncertainty",
            "air_temperature_total_uncertainty",
            "altitude",
            "altitude_total_uncertainty",
            "eastward_wind_component",
            "frost_point_temperature",
            "geopotential_height",
            "northward_wind_component",
            "relative_humidity",
            "relative_humidity_effective_vertical_resolution",
            "relative_humidity_post_processing_radiation_correction",
            "relative_humidity_random_uncertainty",
            "relative_humidity_systematic_uncertainty",
            "relative_humidity_total_uncertainty",
            "shortwave_radiation",
            "shortwave_radiation_total_uncertainty",
            "vertical_speed_of_radiosonde",
            "water_vapor_volume_mixing_ratio",
            "wind_from_direction",
            "wind_from_direction_total_uncertainty",
            "wind_speed",
            "wind_speed_total_uncertainty",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
    )
    def __init__(
        self,
        bbox=None,
        day=None,
        format_=None,
        month=None,
        variable=None,
        year=None,
        limit=None,
    ):
        super().__init__(
            bbox=bbox,
            day=day,
            format_=format_,
            month=month,
            variable=variable,
            year=year,
            limit=limit,
        )
