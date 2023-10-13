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
