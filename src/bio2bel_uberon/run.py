# -*- coding: utf-8 -*-

from ols_client import get_labels
from pybel.constants import NAMESPACE_DOMAIN_OTHER
from pybel_tools.definition_utils import write_namespace
from pybel_tools.resources import deploy_namespace, get_today_arty_namespace

MODULE_NAME = 'uberon'


def deploy_to_arty(ols_base=None):
    """Gets the data and writes BEL namespace file to artifactory"""
    values = get_labels('hp', ols_base=ols_base)

    file_name = get_today_arty_namespace(MODULE_NAME)

    with open(file_name, 'w') as file:
        write_namespace(
            namespace_name='Uber Anatomy Ontology',
            namespace_keyword='UBERON',
            namespace_domain=NAMESPACE_DOMAIN_OTHER,
            author_name='Charles Tapley Hoyt',
            author_contact='charles.hoyt@scai.fraunhofer.de',
            author_copyright='Creative Commons by 4.0',
            citation_name='Uber Anatomy Ontology',
            values=values,
            functions='A',
            file=file
        )

    deploy_namespace(file_name, MODULE_NAME)


if __name__ == '__main__':
    deploy_to_arty()
