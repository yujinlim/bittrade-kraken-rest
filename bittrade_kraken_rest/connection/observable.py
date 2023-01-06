from typing import Optional
from reactivex import Observable
from reactivex.abc import ObserverBase, SchedulerBase
import requests
from reactivex.scheduler import CurrentThreadScheduler

API_URL = 'https://api.kraken.com'

session = requests.Session()

def send_public(url: str, *, session_: Optional[requests.Session]=None, **kwargs) -> Observable[requests.Response]:
    _session = session_ or session
    def subscribe(observer: ObserverBase, scheduler: Optional[SchedulerBase]=None):
        scheduler_ = scheduler or CurrentThreadScheduler()
        def action(*_):
            response = _session.get(f'{API_URL}{url}', params=kwargs)
            if response.ok:
                observer.on_next(response)
                observer.on_completed()
            else:
                try:
                    response.raise_for_status()
                except Exception as exc:
                    observer.on_error(exc)
        scheduler_.schedule(action)
    return Observable(subscribe)