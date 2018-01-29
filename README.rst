Bio2BEL UBERON |build| |coverage| |docs|
========================================
Converts the Uber Anatomy Ontology (UBERON) to BEL

Abstract
--------
We present Uberon, an integrated cross-species ontology consisting of over 6,500 classes representing a variety of
anatomical entities, organized according to traditional anatomical classification criteria. The ontology represents
structures in a species-neutral way and includes extensive associations to existing species-centric anatomical
ontologies, allowing integration of model organism and human data. Uberon provides a necessary bridge between
anatomical structures in different taxa for cross-species inference. It uses novel methods for representing taxonomic
variation, and has proved to be essential for translational phenotype analyses.

Installation
------------
:code:`pip3 install git+https://github.com/bio2bel/uberon.git`

Write Namespace
---------------
:code:`bio2bel_uberon write -o ~/Desktop/uberon.belns`

Deploy to Artifactory
---------------------
:code:`bio2bel_uberon deploy`

.. |build| image:: https://travis-ci.org/bio2bel/uberon.svg?branch=master
    :target: https://travis-ci.org/bio2bel/uberon
    :alt: Build Status

.. |coverage| image:: https://codecov.io/gh/bio2bel/uberon/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/uberon?branch=master
    :alt: Coverage Status

.. |docs| image:: http://readthedocs.org/projects/bio2bel-uberon/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/uberon/en/latest/?badge=latest
    :alt: Documentation Status
