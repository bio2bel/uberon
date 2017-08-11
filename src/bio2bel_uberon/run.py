# -*- coding: utf-8 -*-

from pybel.constants import NAMESPACE_DOMAIN_OTHER
from pybel_tools.ols_utils import OlsNamespaceOntology

__all__ = [
    'MODULE_NAME',
    'MODULE_DOMAIN',
    'MODULE_FUNCTIONS',
    'write_belns',
    'deploy_to_arty',
]

MODULE_NAME = 'uberon'
MODULE_DOMAIN = NAMESPACE_DOMAIN_OTHER
MODULE_FUNCTIONS = 'A'

metadata = {
    'ontology_name': MODULE_NAME,
    'namespace_domain': MODULE_DOMAIN,
    'functions': MODULE_FUNCTIONS,
}

ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, MODULE_FUNCTIONS)

write_belns = ontology.write
deploy_to_arty = ontology.deploy
