************
Installation
************

Decogo is tested on Python 3.8 (CPython).

Dependencies
============

Pyomo
-----
Decogo uses `Pyomo <http://www.pyomo.org/>`_ of version >= 5.7.1.

Solvers
-------
Decogo uses MINLP, NLP and MIP solvers which can interface with Pyomo.
We recommend the following solvers:

- MIP:
    + `Gurobi <https://www.gurobi.com/>`_ (install using ``conda``)

- NLP:
    + `IPOPT <https://github.com/coin-or/Ipopt>`_ (needs version that supports AMPL, see AMPL website)

- MINLP:
    + `SCIP <https://www.scipopt.org/>`_ (needs version that supports AMPL)

Other Python packages
---------------------
It is necessary to have installed the following Python packages:

* ``networkx``
* ``numpy``
* ``scipy``
* ``sympy``

Installation for development in Windows
=======================================

* Install `Git <https://gitforwindows.org/>`_
* Install Python 3.7 with `Anaconda distribution <https://www.anaconda.com/products/individual#windows>`_
* Python IDE: `PyCharm <https://www.jetbrains.com/pycharm/>`_ (full version with institution email is free) is recommended, however you are free to use any IDE you prefer
* Download SCIP, IPOPT executables that support AMPL interface. Put executables either into system folder (C:\\Windows\\System32) or add executable location to PATH variable
* Install Gurobi with ``conda``
