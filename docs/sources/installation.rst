************
Installation
************

Decogo is tested on Python 3.8 (CPython).

Dependencies
============

Pyomo
-----
Decogo uses `Pyomo <http://www.pyomo.org/>`_ of version >= 6.0 (tested up to 6.0.1)

Solvers
-------
Decogo uses MINLP, NLP and MIP solvers which can interface with Pyomo.
We recommend the following solvers:

- MIP:
    + `Gurobi <https://www.gurobi.com/>`_

- NLP:
    + `IPOPT <https://anaconda.org/conda-forge/ipopt>`_ (install using ``conda``)

- MINLP:
    + `SCIP <https://www.scipopt.org/>`_ (needs version that supports AMPL)

Other Python packages
---------------------
It is necessary to have installed the following Python packages:

* ``scipy``
* ``numpy``
* ``pandas``
* ``psutil``
* ``pyutilib``
* ``networkx``

Installation for development in Windows
=======================================

* Install `Git <https://gitforwindows.org/>`_
* Install Python 3.8 with `Anaconda distribution <https://www.anaconda.com/products/individual#windows>`_
* Python IDE: `PyCharm <https://www.jetbrains.com/pycharm/>`_ (full version with institution email is free) is recommended, however you are free to use any IDE you prefer
* Install Gurobi Optimizer software (academic license is free) and choose one of the python installation options
* Install ipopt using ``conda``
* Download SCIP executable that support AMPL interface. Put executables either into system folder (C:\\Windows\\System32) or add executable location to PATH variable