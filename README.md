## climetlab-wekeo_datasets

A dataset plugin for climetlab for the datasets available on WEkEO.

For installation and usage instructions, please refer to [the documentation](https://climetlab-wekeo-datasets.readthedocs.io/).

Currently, the plugin supports CMLS, ECMWF and CMES datasets.

Features
--------

This plugin provides a simple access to the datasets provided by WEkEO.

To narrow down the data to download, users can specify a start and an end date.

While it is not mandatory, the usage of Dask is recommended.

For usage examples, please refer to the [demo notebook](https://github.com/wekeo/climetlab-wekeo-datasets/tree/main/notebooks/demo_main.ipynb)

## Datasets description

The list of supported datasets can be seen in the setup.py file.
Each item in the entry points list refers to a specific datasets.

The descriptions can be retrieved directly from [WEkEO](https://www.wekeo.eu/data)

## Using climetlab to access the data

See the [demo notebooks](https://github.com/wekeo/climetlab-wekeo-datasets/tree/main/notebooks)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wekeo/climetlab-wekeo-datasets/main?urlpath=lab)


- [demo_main.ipynb](https://github.com/wekeo/climetlab-wekeo-datasets/tree/main/notebooks/demo_main.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/wekeo/climetlab-wekeo-datasets/blob/main/notebooks/demo_main.ipynb)
[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wekeo/climetlab-wekeo-datasets/blob/main/notebooks/demo_main.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wekeo/climetlab-wekeo-datasets/main?filepath=notebooks/demo_main.ipynb)
[<img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg">](https://deepnote.com/launch?name=MyProject&url=https://github.com/wekeo/climetlab-wekeo-datasets/tree/main/notebooks/demo_main.ipynb)


The climetlab python package allows easy access to the data with a few lines of code such as:
``` python

!pip install climetlab climetlab-wekeo-datasets
import climetlab as cml
ds = cml.load_dataset(
    "wekeo-datasets-cgls-hourly-lst-global-v2",
    start="2021-01-18",
    end="2021-01-19",
)
ds.to_xarray(xarray_open_mfdataset_kwargs={"chunks": "auto", "engine": "netcdf4"})


Support and contributing
------------------------

Please open a issue on github if this is a github repository.

LICENSE
-------

See the LICENSE file.
(C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
This software is licensed under the terms of the Apache Licence Version 2.0
which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
In applying this licence, ECMWF does not waive the privileges and immunities
granted to it by virtue of its status as an intergovernmental organisation
nor does it submit to any jurisdiction.

Authors
-------

Germano Guerrini and al.

See also the CONTRIBUTORS.md file.
