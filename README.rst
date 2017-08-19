UBERON to BEL
=============
Convert the Uber Anatomy Ontology (UBERON) to a BEL

Citation
--------
Gasteiger, E., Gattiker, A., Hoogland, C., Ivanyi, I., Appel, R. D., & Bairoch, A. (2003). ExPASy: The proteomics server for in-depth protein knowledge and analysis. Nucleic Acids Research, 31(13), 3784–8. Retrieved from http://www.ncbi.nlm.nih.gov/pubmed/12824418

Evidence
--------
We present Uberon, an integrated cross-species ontology consisting of over 6,500 classes representing a variety of anatomical entities, organized according to traditional anatomical classification criteria. The ontology represents structures in a species-neutral way and includes extensive associations to existing species-centric anatomical ontologies, allowing integration of model organism and human data. Uberon provides a necessary bridge between anatomical structures in different taxa for cross-species inference. It uses novel methods for representing taxonomic variation, and has proved to be essential for translational phenotype analyses.

Installation
------------
:code:`pip3 install git+https://github.com/bio2bel/uberon.git`

Write Namespace
---------------
:code:`bio2bel_uberon write -o ~/Desktop/uberon.belns`

Deploy to Artifactory
---------------------
:code:`bio2bel_uberon deploy`
