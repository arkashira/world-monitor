from dataclasses import dataclass
from typing import List
import time

@dataclass
class Event:
    timestamp: float
    data: str

class WorldMonitor:
    def __init__(self):
        self.events = []
        self.latency = 0

    def add_event(self, event: Event):
        start_time = time.time()
        self.events.append(event)
        end_time = time.time()
        self.latency = (end_time - start_time) * 1000

    def get_latency(self) -> float:
        return self.latency

    def get_events_per_second(self) -> int:
        if not self.events:
            return 0
        return len(self.events) / (self.events[-1].timestamp - self.events[0].timestamp)

    def is_reliable(self) -> bool:
        return all(event.timestamp < self.events[-1].timestamp for event in self.events[:-1])
