from typing import Optional
from reactivex import Observable
from reactivex.abc import ObserverBase, SchedulerBase
import requests
from reactivex.scheduler import CurrentThreadScheduler

API_URL = 'https://api.kraken.com'

_session = requests.Session()

def send_public(url: str, *, session: Optional[requests.Session]=None, **kwargs) -> Observable[requests.Response]:
    request = requests.Request(
        'GET',
        f'{API_URL}{url}',
        params=kwargs
    )
    return send(request.prepare(), session_=session)

def send(request: requests.PreparedRequest, *, session_: Optional[requests.Session]=None) -> Observable[requests.Response]:
    session = session_ or _session
    def subscribe(observer: ObserverBase, scheduler: Optional[SchedulerBase]=None):
        scheduler_ = scheduler or CurrentThreadScheduler()
        def action(*_):
            response = session.send(request)
            if response.ok:
                as_json = response.json()
                if not as_json['error']:
                    observer.on_next(response)
                    observer.on_completed()
                else:
                    observer.on_error(Exception(as_json['error'][0]))
            else:
                try:
                    response.raise_for_status()
                except Exception as exc:
                    observer.on_error(exc)
        scheduler_.schedule(action)
    return Observable(subscribe)