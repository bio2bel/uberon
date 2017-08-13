# -*- coding: utf-8 -*-

from __future__ import print_function

import logging

import click
import sys
from ols_client import OLS_BASE
from pybel_tools.ols_utils import OlsNamespaceOntology

from .run import MODULE_FUNCTIONS, MODULE_DOMAIN, MODULE_NAME


@click.group()
@click.option('-b', '--ols-base', help="OLS base url. Defaults to {}".format(OLS_BASE))
def main():
    """Uber Anatomy Ontology to BEL"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")


@main.command()
@click.option('-b', '--ols-base', help="OLS base url. Defaults to {}".format(OLS_BASE))
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
def write(ols_base, output):
    """Writes BEL namespace"""
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, MODULE_FUNCTIONS, ols_base=ols_base)
    ontology.write(output)


@main.command()
@click.option('-b', '--ols-base', help="OLS base url. Defaults to {}".format(OLS_BASE))
@click.option('--no-hash-check', is_flag=True)
def deploy(ols_base=None, no_hash_check=False):
    """Deploy to Artifactory"""
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, MODULE_FUNCTIONS, ols_base=ols_base)
    success = ontology.deploy(hash_check=(not no_hash_check))
    click.echo('Deployed to {}'.format(success) if success else 'Duplicate not deployed')


if __name__ == '__main__':
    main()
