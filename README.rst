===========================
distsim
===========================

.. image:: https://img.shields.io/travis/mikulatomas/distsim.svg
        :target: https://travis-ci.org/mikulatomas/distsim.svg?branch=master

.. image:: https://codecov.io/gh/mikulatomas/distsim/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/mikulatomas/distsim

.. image:: https://img.shields.io/github/license/mikulatomas/distsim
        :target: https://opensource.org/licenses/MIT


Simple simulator of distributed system.


Installation
------------

.. code:: bash

        $ git clone https://github.com/mikulatomas/distsim
        $ cd distsim
        $ pip install -e .


Development
-----------
Clone this repository to the folder, then:

.. code:: bash

        # create virtualenv (optional)
        $ mkvirtualenv distsim -p python3

        #if is not actived (optional)
        $ workon distsim 

        $ pip install -e .

        $ python setup.py test
