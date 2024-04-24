Installation
============

Get your credentials
--------------------

1. If you don't have a WEkEO account, please self register at the WEkEO `registration page <https://www.wekeo.eu/web/guest/user-registration>`_, then proceed to the step below.

2. Copy the code below in the file `$HOME/.hdarc` in your Unix/Linux environment. Adapt the following template with the credentials of your WEkEO account:

    .. code-block:: ini

        user: [username]
        password: [password]

Plugin installation
-------------------
The plugin requires both CliMetLab and a companion source plugin to access WEkEO data.
To better understand the difference between a dataset and a source plugin, please refer to the official `CliMetLab documentation <https://climetlab.readthedocs.io/en/latest/contributing/overview.html>`_.

Both dependencies are installed automatically via *pip*:

    .. code-block:: shell

        pip install climetlab-wekeo-datasets

