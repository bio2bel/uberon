# -*- coding: utf-8 -*-

from __future__ import print_function

import logging
import sys

import click

from ols_client import OLS_BASE
from pybel_tools.ols_utils import OlsNamespaceOntology
from .run import MODULE_FUNCTIONS, MODULE_DOMAIN, MODULE_NAME


@click.group()
@click.option('-b', '--ols-base', help="OLS base url. Defaults to {}".format(OLS_BASE))
@click.pass_context
def main(ctx, ols_base):
    """Utilities for UBERON BEL namespace generation"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")
    ctx.obj = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, MODULE_FUNCTIONS, ols_base=ols_base)


@main.command()
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
@click.pass_context
def write(ctx, output):
    """Writes BEL namespace"""
    ctx.obj.write(output)


@main.command()
@click.option('--no-hash-check', is_flag=True)
@click.pass_context
def deploy(ctx, no_hash_check):
    """Deploy to Artifactory"""
    success = ctx.obj.deploy(hash_check=(not no_hash_check))
    click.echo('Deployed to {}'.format(success) if success else 'Duplicate not deployed')


if __name__ == '__main__':
    main()
