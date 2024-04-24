#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from unittest.mock import patch

import climetlab as cml


def test_read():
    with patch("climetlab.load_source"):
        ds = cml.load_dataset(
            "wekeo-clms-clms-global-albh-1km-v1-10daily-netcdf",
            start="2021-01-18",
            end="2021-01-19",
        )
        xds = ds.to_xarray()
        print(xds)


if __name__ == "__main__":
    test_read()
