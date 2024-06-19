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


class clms_global_lst_5km_v2_hourly_netcdf(Main):
    name = "EO:CLMS:DAT:CLMS_GLOBAL_LST_5KM_V2_HOURLY_NETCDF"
    dataset = "EO:CLMS:DAT:CLMS_GLOBAL_LST_5KM_V2_HOURLY_NETCDF"

    @normalize(
        "acquisitionType",
        [
            "NOMINAL",
        ],
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize(
        "platform",
        [
            "GOES",
            "GOES-16",
            "GOES-17",
            "GOES-R",
            "HIMAWARI",
            "HIMAWARI-8",
            "HIMAWARI-9",
            "MSG",
            "MSG-1",
            "MSG-2",
            "MSG-3",
            "MSG-4",
            "MTSAT",
        ],
        multiple=True,
    )
    @normalize(
        "processingCenter",
        [
            "IPMA",
        ],
    )
    @normalize(
        "productType",
        [
            "LST",
        ],
    )
    @normalize(
        "productionStatus",
        [
            "ARCHIVED",
            "CANCELLED",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        acquisitionType=None,
        bbox=None,
        end=None,
        platform=None,
        processingCenter=None,
        productType=None,
        productionStatus=None,
        start=None,
        limit=None,
    ):
        super().__init__(
            acquisitionType=acquisitionType,
            bbox=bbox,
            end=end,
            platform=platform,
            processingCenter=processingCenter,
            productType=productType,
            productionStatus=productionStatus,
            start=start,
            limit=limit,
        )
