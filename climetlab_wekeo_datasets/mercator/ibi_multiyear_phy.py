#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.mercator.main import Main

LAYERS = [
    "cmems_mod_ibi_phy_my_0.083deg-2D_PT1H-m_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-2D_PT1H-m
    "cmems_mod_ibi_phy_my_0.083deg-3D-climatology_P1M-m_202211",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D-climatology_P1M-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_P1D-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m_202012",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_P1M-m
    "cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m_202211",  # noqa: E501 cmems_mod_ibi_phy_my_0.083deg-3D_P1Y-m
]


class ibi_multiyear_phy(Main):
    name = "EO:MO:DAT:IBI_MULTIYEAR_PHY_005_002"
    dataset = "EO:MO:DAT:IBI_MULTIYEAR_PHY_005_002"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "bottomT",
            "bottomT_mean",
            "bottomT_standard_deviation",
            "mlotst",
            "mlotst_mean",
            "mlotst_standard_deviation",
            "so",
            "so_mean",
            "so_standard_deviation",
            "thetao",
            "thetao_mean",
            "thetao_standard_deviation",
            "ubar",
            "uo",
            "uo_mean",
            "uo_standard_deviation",
            "vbar",
            "vo",
            "vo_mean",
            "vo_standard_deviation",
            "zos",
            "zos_mean",
            "zos_standard_deviation",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-0.5057600140571594",
            "-1.5558552742004395",
            "-1045.854248046875",
            "-108.03028106689453",
            "-11.773679733276367",
            "-1265.8614501953125",
            "-13.99103832244873",
            "-133.07582092285156",
            "-1387.376953125",
            "-16.52532196044922",
            "-163.16445922851562",
            "-1652.5684814453125",
            "-180.5499267578125",
            "-19.42980194091797",
            "-1945.2955322265625",
            "-2.6676816940307617",
            "-22.75761604309082",
            "-221.14117431640625",
            "-2262.421630859375",
            "-26.558300018310547",
            "-2600.38037109375",
            "-271.35638427734375",
            "-2776.039306640625",
            "-3.8562798500061035",
            "-30.874561309814453",
            "-3138.56494140625",
            "-333.8628234863281",
            "-35.740203857421875",
            "-3513.445556640625",
            "-370.6884765625",
            "-4093.15869140625",
            "-41.180023193359375",
            "-4488.15478515625",
            "-457.6256103515625",
            "-47.21189498901367",
            "-4888.06982421875",
            "-5.140361309051514",
            "-5291.68310546875",
            "-53.85063552856445",
            "-565.2922973632812",
            "-5698.060546875",
            "-6.543033599853516",
            "-61.11283874511719",
            "-628.0260009765625",
            "-77.61116027832031",
            "-773.3682861328125",
            "-8.09251880645752",
            "-9.822750091552734",
            "-947.4478759765625",
            "-97.04131317138672",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-0.5057600140571594",
            "-1.5558552742004395",
            "-1045.854248046875",
            "-108.03028106689453",
            "-11.773679733276367",
            "-1265.8614501953125",
            "-13.99103832244873",
            "-133.07582092285156",
            "-1387.376953125",
            "-16.52532196044922",
            "-163.16445922851562",
            "-1652.5684814453125",
            "-180.5499267578125",
            "-19.42980194091797",
            "-1945.2955322265625",
            "-2.6676816940307617",
            "-22.75761604309082",
            "-221.14117431640625",
            "-2262.421630859375",
            "-26.558300018310547",
            "-2600.38037109375",
            "-271.35638427734375",
            "-2776.039306640625",
            "-3.8562798500061035",
            "-30.874561309814453",
            "-3138.56494140625",
            "-333.8628234863281",
            "-35.740203857421875",
            "-3513.445556640625",
            "-370.6884765625",
            "-4093.15869140625",
            "-41.180023193359375",
            "-4488.15478515625",
            "-457.6256103515625",
            "-47.21189498901367",
            "-4888.06982421875",
            "-5.140361309051514",
            "-5291.68310546875",
            "-53.85063552856445",
            "-565.2922973632812",
            "-5698.060546875",
            "-6.543033599853516",
            "-61.11283874511719",
            "-628.0260009765625",
            "-77.61116027832031",
            "-773.3682861328125",
            "-8.09251880645752",
            "-9.822750091552734",
            "-947.4478759765625",
            "-97.04131317138672",
        ],
    )
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        maximum_depth=None,
        minimum_depth=None,
        end_datetime="2021-12-28T00:00:00Z",
        start_datetime="1993-01-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            maximum_depth=maximum_depth,
            minimum_depth=minimum_depth,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
