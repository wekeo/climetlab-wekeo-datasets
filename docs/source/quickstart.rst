Quick start
===========

Once the plugin is installed, it can be used directly into a Jupyter notebook.


.. code-block:: python

    import climetlab as cml
    from dask.distributed import Client

    # Instantiate a default Dask distributed client to handle data
    client = Client()

    cmlds = cml.load_dataset(
        "wekeo-clms-cgls-hourly-lst-global-v2",
        start="2021-01-18",
        end="2021-01-19",
    )

    ds = cmlds.to_xarray()
    ds.LST.plot(x="lon", y="lat")

    client.shutdown()

.. image:: ../images/plot.png
    :width: 400

To ease the construct of the arguments for the `load_dataset` function, especially for those
datasets with a lot of options, you can use a utility function that transforms an HDA
API request into usable parameters.

Open the WEkEO Data web page, choose one of the supported dataset and select the parameters in
the form, then click on the **Show API request(s)** button:

.. image:: ../images/wekeo_ui_show_request.png

On the new modal, click the **Copy** button:

.. image:: ../images/wekeo_ui_copy_request.png

Once the request is copied into the clipboard, you can use it following the example below:

.. code-block:: python

    import climetlab as cml
    from climetlab_wekeo_datasets import hda2cml

    query = {
        "datasetId": "EO:ECMWF:DAT:CAMS_EUROPE_AIR_QUALITY_FORECASTS",
        "boundingBoxValues": [
            {
            "name": "area",
            "bbox": [
                3.694591996044645,
                35.907220595373886,
                14.939002418789217,
                42.61449357770201
            ]}
        ],
        "dateRangeSelectValues": [
            {
                "name": "date",
                "start": "2023-08-25T00:00:00.000Z",
                "end": "2023-10-31T23:59:59.999Z"
            }
        ],
        "multiStringSelectValues": [
            {
            "name": "variable",
            "value": [
                "alder_pollen",
                "ammonia"
            ]},
            ...
        ],
        "stringChoiceValues": [
            {
                "name": "format",
                "value": "netcdf"
            }
        ]
    }

    entry_point, arguments = hda2cml(query)
    dataset = cml.load_dataset(entry_point, **arguments)