from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Callable


class Event(ABC):
    @staticmethod
    @abstractmethod
    def name() -> str:
        pass

    @abstractmethod
    def payload(self) -> Any:
        pass


class EventListener(ABC):
    @abstractmethod
    def on_event(self, event: Event) -> None:
        pass


EventListenerFunction = Callable[[Event], Any]


@dataclass
class EventManager:
    _listeners: dict[str, list[EventListener | EventListenerFunction]] = field(default_factory=dict)

    def attach(self, event_name: str, listener: EventListener | EventListenerFunction) -> None:
        if event_name in self._listeners:
            self._listeners[event_name].append(listener)
        else:
            self._listeners[event_name] = [listener]

    def detach(self, event_type: str, listener: EventListener | EventListenerFunction) -> None:
        self._listeners[event_type].remove(listener)

    def notify(self, event: Event):
        for listener in self._listeners.get(event.name()) or ():
            if listener is EventListener:
                listener.on_event(event)
            else:
                listener(event)
