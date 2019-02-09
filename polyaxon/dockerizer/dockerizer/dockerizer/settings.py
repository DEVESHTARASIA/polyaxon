import json
import os

import rhea
from rhea import RheaError
from rhea.specs import UriSpec

from unipath import Path


def base_directory():
    return Path(__file__).ancestor(3)


ROOT_DIR = base_directory()
ENV_VARS_DIR = ROOT_DIR.child('env_vars')

config_values = [
    '{}/default.json'.format(ENV_VARS_DIR),
    os.environ,
]

if os.path.isfile('{}/local.json'.format(ENV_VARS_DIR)):
    config_values.append('{}/local.json'.format(ENV_VARS_DIR))

config = rhea.Rhea.read_configs(config_values)

K8S_NAMESPACE = config.get_string('POLYAXON_K8S_NAMESPACE')
MOUNT_PATHS_NVIDIA = config.get_string('POLYAXON_MOUNT_PATHS_NVIDIA', is_optional=True)
REPO_DOWNLOAD_URL = config.get_string('POLYAXON_REPO_DOWNLOAD_URL')
REPO_IS_INTERNAL = config.get_boolean('POLYAXON_REPO_IS_INTERNAL')
REPO_COMMIT = config.get_boolean('POLYAXON_REPO_COMMIT')
CONTAINER_FROM_IMAGE = config.get_string('POLYAXON_CONTAINER_FROM_IMAGE')
CONTAINER_IMAGE_TAG = config.get_string('POLYAXON_CONTAINER_IMAGE_TAG')
CONTAINER_IMAGE_NAME = config.get_string('POLYAXON_CONTAINER_IMAGE_NAME')
CONTAINER_BUILD_STEPS = config.get_list('POLYAXON_CONTAINER_BUILD_STEPS', is_optional=True)
CONTAINER_ENV_VARS = config.get_string('POLYAXON_CONTAINER_ENV_VARS',
                                       is_list=True,
                                       is_optional=True)
CONTAINER_NO_CACHE = config.get_boolean('POLYAXON_CONTAINER_NO_CACHE',
                                        is_optional=True,
                                        default=False)

REGISTRY_USER = config.get_string('POLYAXON_REGISTRY_USER', is_optional=True)
REGISTRY_PASSWORD = config.get_string('POLYAXON_REGISTRY_PASSWORD', is_optional=True)
REGISTRY_HOST_NAME = config.get_string('POLYAXON_REGISTRY_HOST', is_optional=True)

# This is duplicated
PRIVATE_REGISTRIES_PREFIX = 'POLYAXON_PRIVATE_REGISTRY_'


def get_external_registries():
    registries = []
    for key in config.keys_startswith(PRIVATE_REGISTRIES_PREFIX):

        try:
            registry_dict = config.get_dict(key, is_secret=True)
            registry_spec = UriSpec(**registry_dict)
        except RheaError:
            registry_spec = config.get_string(key, is_secret=True)
            try:
                # We might get this value from a chart with `toJson` applied.
                registry_spec = json.loads(registry_spec)
            except json.decoder.JSONDecodeError:
                pass

            registry_spec = config.parse_uri_spec(registry_spec)

        if registry_spec:
            registries.append(registry_spec)

    return registries


PRIVATE_REGISTRIES = get_external_registries()
