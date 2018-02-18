# -*- coding: utf-8 -*-

from pybel.constants import ABUNDANCE, NAMESPACE_DOMAIN_OTHER
from pybel_tools.ols_utils import OlsNamespaceOntology

__all__ = [
    'MODULE_NAME',
    'MODULE_DOMAIN',
    'MODULE_FUNCTION',
    'write_belns',
    'deploy_to_arty',
]

MODULE_NAME = 'uberon'
MODULE_DOMAIN = NAMESPACE_DOMAIN_OTHER
MODULE_FUNCTION = ABUNDANCE


def write_belns(file):
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, bel_function=MODULE_FUNCTION)
    return ontology.write_namespace(file)


def deploy_to_arty():
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, bel_function=MODULE_FUNCTION)
    return ontology.deploy_namespace()
