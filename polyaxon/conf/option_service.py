from typing import Any

from hestia.service_interface import Service
from rhea import RheaError

from conf.conf_manager import conf_cache_manager
from conf.exceptions import ConfException
from conf.option_manager import option_manager


class OptionService(Service):
    __all__ = ('get', 'set', 'delete', 'clear_cache')

    option_manager = option_manager
    cache_manager = conf_cache_manager
    service_name = 'Option'

    def __init__(self):
        self.stores = {}

    def get_options_handler(self):
        return None

    def can_handle(self, key: str) -> bool:
        return isinstance(key, str) and self.option_manager.knows(key=key)

    def get_option(self, key: str, ) -> 'Option':
        return self.option_manager.get(key=key)

    def get_store(self, option: 'Option') -> Any:
        if option.store not in self.stores:
            raise ConfException('Option `{}` has an invalid store.'.format(option.key))

        return self.stores[option.store]

    @staticmethod
    def _get_value(option, value, to_dict):
        if not to_dict:
            return value
        option_dict = option.to_dict(value=value)
        return option_dict

    def get(self, key: str, check_cache=True, to_dict=False) -> Any:
        if not self.is_setup:
            return
        if not self.can_handle(key=key):
            raise ConfException('{} service request an unknown key `{}`.'.format(
                self.service_name, key))

        option = self.get_option(key=key)

        if check_cache:
            value = self.cache_manager.get_from_cache(key=key)
            if self.cache_manager.is_valid_value(value=value):
                return self._get_value(option=option, value=value, to_dict=to_dict)

        store = self.get_store(option=option)
        value = store.get(option=option)

        # Cache value
        self.cache_manager.set_to_cache(key=key, value=value, ttl=option.cache_ttl)

        return self._get_value(option=option, value=value, to_dict=to_dict)

    def set(self, key: str, value: Any) -> None:
        if not self.is_setup:
            return
        if not self.can_handle(key=key):
            raise ConfException('{} service request an unknown key `{}`.'.format(
                self.service_name, key))
        if value is None:
            raise ConfException('{} service requires a value for key `{}` to set.'.format(
                self.service_name, key))
        option = self.get_option(key=key)
        # Convert value
        try:
            value = option.parse(value=value)
        except RheaError as e:
            raise ConfException(e)

        store = self.get_store(option=option)
        store.set(option=option, value=value)
        # Cache value
        self.cache_manager.set_to_cache(key=key, value=value, ttl=option.cache_ttl)

    def delete(self, key: str) -> None:
        if not self.is_setup:
            return
        if not self.can_handle(key=key):
            raise ConfException('{} service request an unknown key `{}`.'.format(
                self.service_name, key))

        option = self.get_option(key=key)
        store = self.get_store(option=option)
        store.delete(option=option)
        # Clear Cache key
        self.cache_manager.clear_key(key=key)

    def clear_cache(self) -> None:
        self.cache_manager.clear()
