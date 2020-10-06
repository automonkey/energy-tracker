import argparse
import logging
import sys
import warnings
from enum import Enum

from energy_tracker_build.src.api_deploy_cli import ApiDeployCli

logger = logging.getLogger(__name__)


class BuildCommand(Enum):
    deployApi = "deploy-api"

    def __str__(self):
        return self.value


class DeployEnvironment(Enum):
    dev = "dev"

    def __str__(self):
        return self.value


def main():
    args = parse_args()
    ApiDeployCli().deploy(env=args.env)


def parse_args():
    args = create_parser().parse_args()
    init_logging(args.verbosity)
    logger.debug("args: %s", args)

    return args


def create_parser():
    parser = argparse.ArgumentParser(description="Build and deployment utilities for Energy Tracker.")

    parser.add_argument("command", type=BuildCommand, choices=list(BuildCommand), help="The command to run")

    parser.add_argument(
        "--env",
        type=DeployEnvironment,
        default=DeployEnvironment.dev,
        choices=list(DeployEnvironment),
        help="The deploy environment",
    )

    parser.add_argument(
        "-v",
        "--verbosity",
        action="count",
        default=0,
        help="Specify up to three times to increase verbosity, "
        "i.e. -v to see warnings, -vv for information messages, "
        "or -vvv for debug messages.",
    )

    return parser


def init_logging(verbosity, stream=sys.stdout, silence_packages=()):
    LOG_LEVELS = [logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
    level = LOG_LEVELS[min(verbosity, len(LOG_LEVELS) - 1)]
    msg_format = "%(message)s"
    if level == logging.DEBUG:
        warnings.filterwarnings("ignore")
        msg_format = "%(asctime)s %(levelname)-8s %(name)s " "%(module)s.py:%(funcName)s():%(lineno)d %(message)s"
    logging.basicConfig(level=level, format=msg_format, stream=stream)

    for package in silence_packages:
        logging.getLogger(package).setLevel(max([level, logging.WARNING]))
