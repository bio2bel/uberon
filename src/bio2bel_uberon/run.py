# -*- coding: utf-8 -*-

from ols_client import get_labels, get_metadata
from pybel.constants import NAMESPACE_DOMAIN_OTHER
from pybel_tools.definition_utils import write_namespace
from pybel_tools.resources import deploy_namespace, get_today_arty_namespace

__all__ = [
    'MODULE_NAME',
    'write_belns',
    'deploy_to_arty',
]

MODULE_NAME = 'uberon'


def write_belns(file, ols_base=None):
    """Serializes UBERON to a BEL namespace.

    :param file file: A write-enable file or file-like
    :param str ols_base: An optional, custom OLS base url
    """
    metadata = get_metadata(MODULE_NAME, ols_base=ols_base)
    values = get_labels(MODULE_NAME, ols_base=ols_base)

    config = metadata['config']

    write_namespace(
        namespace_name=config['title'],
        namespace_keyword=config['preferredPrefix'],
        namespace_domain=NAMESPACE_DOMAIN_OTHER,
        namespace_description=config['description'],
        namespace_version=config['version'],
        citation_name=config['title'],
        citation_url=config['versionIri'],
        author_name='Charles Tapley Hoyt',
        author_contact='charles.hoyt@scai.fraunhofer.de',
        author_copyright='Creative Commons by 4.0',
        values=values,
        functions='A',
        file=file
    )


def deploy_to_arty(ols_base=None):
    """Gets the data and writes BEL namespace file to Artifactory

    :param str ols_base: An optional, custom OLS base url
    """
    file_name = get_today_arty_namespace(MODULE_NAME)

    with open(file_name, 'w') as file:
        write_belns(file, ols_base=ols_base)

    deploy_namespace(file_name, MODULE_NAME)


if __name__ == '__main__':
    deploy_to_arty()
