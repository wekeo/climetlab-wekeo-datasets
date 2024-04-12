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


class clms_global_ndvi_300m_v1_10daily_netcdf(Main):
    name = "EO:CLMS:DAT:CLMS_GLOBAL_NDVI_300M_V1_10DAILY_NETCDF"
    dataset = "EO:CLMS:DAT:CLMS_GLOBAL_NDVI_300M_V1_10DAILY_NETCDF"

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
            "NDVI300",
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
            "PROBA-V",
        ],
    )
    @normalize(
        "processingCenter",
        [
            "VITO",
        ],
    )
    def __init__(
        self,
        productionStatus=None,
        start=None,
        end=None,
        bbox=None,
        productType="NDVI300",
        acquisitionType="NOMINAL",
        platform="PROBA-V",
        processingCenter="VITO",
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
