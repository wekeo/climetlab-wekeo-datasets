#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations
from climetlab.decorators import normalize

from climetlab_wekeo_datasets.clms.main import Main


class clms_global_ssm_1km_v1_daily_netcdf(Main):
    name = "EO:CLMS:DAT:CLMS_GLOBAL_SSM_1KM_V1_DAILY_NETCDF"
    dataset = "EO:CLMS:DAT:CLMS_GLOBAL_SSM_1KM_V1_DAILY_NETCDF"

    @normalize(
        "productionStatus",
        [
            "ARCHIVED",
            "CANCELLED",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "productType",
        [
            "SSM1km",
        ],
    )
    @normalize(
        "acquisitionType",
        [
            "NOMINAL",
        ],
    )
    @normalize(
        "platform",
        [
            "SENTINEL-1",
        ],
    )
    @normalize(
        "processingCenter",
        [
            "TU_WIEN",
        ],
    )
    def __init__(
        self,
        productionStatus=None,
        start=None,
        end=None,
        bbox=None,
        productType="SSM1km",
        acquisitionType="NOMINAL",
        platform="SENTINEL-1",
        processingCenter="TU_WIEN",
        limit=None,
    ):
        super().__init__(
            productionStatus=productionStatus,
            start=start,
            end=end,
            bbox=bbox,
            productType=productType,
            acquisitionType=acquisitionType,
            platform=platform,
            processingCenter=processingCenter,
            limit=limit,
        )
