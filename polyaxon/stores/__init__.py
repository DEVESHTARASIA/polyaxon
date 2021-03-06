from hestia.service_interface import LazyServiceWrapper

from django.conf import settings

from stores.service import StoresService


def get_paths_backend():
    return settings.STORES_BACKEND or 'stores.service.StoresService'


backend = LazyServiceWrapper(
    backend_base=StoresService,
    backend_path=get_paths_backend(),
    options={}
)
backend.expose(locals())
