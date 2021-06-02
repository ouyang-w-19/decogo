********
Settings
********

The settings names are defined with their default values at the beginning of the
file ``decogo/solver/settings.py``. The settings are grouped by usage:

* Solver names and their settings
* General settings
* OA algorithm
* CG settings

In order to add/modify/remove the settings, simply modify the declaration of dictionary
``_setting_names_default_val`` in ``solver/settings.py``.

In order to overwrite the default settings, it is necessary to provide the settings
file ``decogo.set`` which should be located in the working directory. The example
of settings file definition:

.. parsed-literal::

    strategy = OA
    maxtime = 300

In the example above, we set the solver strategy to OA and set maximum running time 300 sec.

Here is the list of settings defined settings and their default values:

.. literalinclude:: ../../decogo/solver/settings.py
    :language: python
    :lines: 13-72