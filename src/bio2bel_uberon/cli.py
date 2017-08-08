# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_uberon arty`"""

from __future__ import print_function

import logging
import sys

import click

from ols_client import OLS_BASE
from .run import deploy_to_arty, write_belns


@click.group()
def main():
    """Output gene family hierarchy as BEL script and BEL namespace"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")


@main.command()
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
@click.option('-b', '--ols-base', help="OLS base url. Defaults to {}".format(OLS_BASE))
def write(output, ols_base):
    """Writes BEL namespace to standard out"""
    write_belns(output, ols_base=ols_base)


@main.command()
@click.option('-b', '--ols-base', help="OLS base url. Defaults to {}".format(OLS_BASE))
def arty(ols_base):
    """Deploy to artifactory"""
    deploy_to_arty(ols_base=ols_base)


if __name__ == '__main__':
    main()
