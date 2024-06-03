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


class insitu_gridded_observations_europe(Main):
    name = "EO:ECMWF:DAT:INSITU_GRIDDED_OBSERVATIONS_EUROPE"
    dataset = "EO:ECMWF:DAT:INSITU_GRIDDED_OBSERVATIONS_EUROPE"

    @normalize(
        "grid_resolution",
        [
            "0.1deg",
            "0.25deg",
        ],
    )
    @normalize(
        "period",
        [
            "1950_1964",
            "1965_1979",
            "1980_1994",
            "1995_2010",
            "2011_2019",
            "2011_2020",
            "2011_2021",
            "2011_2022",
            "2011_2023",
            "full_period",
        ],
    )
    @normalize(
        "product_type",
        [
            "elevation",
            "ensemble_mean",
            "ensemble_spread",
        ],
    )
    @normalize(
        "variable",
        [
            "land_surface_elevation",
            "maximum_temperature",
            "mean_temperature",
            "minimum_temperature",
            "precipitation_amount",
            "relative_humidity",
            "sea_level_pressure",
            "surface_shortwave_downwelling_radiation",
            "wind_speed",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "21.0e",
            "22.0e",
            "23.1e",
            "24.0e",
            "25.0e",
            "26.0e",
            "27.0e",
            "28.0e",
            "29.0e",
            "29.0e",
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
        grid_resolution,
        period,
        product_type,
        variable,
        version,
        format_=None,
        limit=None,
    ):
        super().__init__(
            grid_resolution=grid_resolution,
            period=period,
            product_type=product_type,
            variable=variable,
            version=version,
            format_=format_,
            limit=limit,
        )
