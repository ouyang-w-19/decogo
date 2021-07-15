.. Decogo documentation master file, created by
   sphinx-quickstart on Fri Mar  6 17:19:37 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


######
Decogo
######
Decogo is a software framework for decomposition-based global optimization of block-separable  MINLP  problems of the form

.. math::
   :nowrap:

   \begin{equation} 
   \min \, c^Tx  : x\in P,\,\, x_k\in X_k,\,\, k\in K 
   \end{equation}

with

.. math::
   :nowrap:

   \begin{equation} 
   P:= \{x \in {\bf R}^{n}: \,  \, a_i^T x\leq b_i,\, i\in M_1,
   \,\, a_i^T x= b_i,\, i\in M_2 \},
   \end{equation}

:math:`|M_1|+|M_2|=m`, and

.. math::
   :nowrap:

   \begin{equation} 
   X_k:=\{ y \in [\underline{x}_k, \overline{x}_k] \subset {\bf R}^{n_{k1}}
   \times {\bf Z}^{n_{k2}}: g_{kj}(y)\leq 0,\, j\in J_k  \}.
   \end{equation}

The vector of variables :math:`x \in {\bf R}^n` is partitioned into :math:`|K|` blocks 
such that :math:`n=\sum\limits_{k \in K}n_k`, where :math:`n_k=n_{k1}+n_{k2}` is the
dimension of block :math:`k`, :math:`n=\sum\limits_{k \in K}n_k` and :math:`x_k\in {\bf R}^{n_k}` denotes the variables of block :math:`k`. 
The vectors :math:`\underline{x}, \overline{x} \in {\bf R}^{n}` denote  lower and 
upper bounds on the variables.

.. toctree::
   :caption: Documentation
   :maxdepth: 1

   sources/installation
   sources/example
   sources/settings
   sources/tests
   sources/modules
   sources/classes

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


