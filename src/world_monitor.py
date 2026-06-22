import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict

@dataclass
class Event:
    timestamp: datetime
    semantic_tag: str
    geographic_region: str

class WorldMonitor:
    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)

    def get_event_throughput(self, time_window: timedelta) -> int:
        recent_events = [event for event in self.events if event.timestamp >= datetime.now() - time_window]
        return len(recent_events)

    def get_events_by_tag(self, semantic_tag: str) -> List[Event]:
        return [event for event in self.events if event.semantic_tag == semantic_tag]

    def get_events_by_region(self, geographic_region: str) -> List[Event]:
        return [event for event in self.events if event.geographic_region == geographic_region]

    def get_grafana_dashboard_template(self) -> Dict:
        return {
            "rows": [
                {
                    "title": "Event Throughput",
                    "panels": [
                        {
                            "id": 1,
                            "title": "Last 5 minutes",
                            "type": "graph",
                            "span": 12,
                            "targets": [
                                {
                                    "expr": "event_throughput{time_window='5m'}",
                                    "legendFormat": "{{job}}",
                                    "refId": "A"
                                }
                            ]
                        },
                        {
                            "id": 2,
                            "title": "Last 1 hour",
                            "type": "graph",
                            "span": 12,
                            "targets": [
                                {
                                    "expr": "event_throughput{time_window='1h'}",
                                    "legendFormat": "{{job}}",
                                    "refId": "B"
                                }
                            ]
                        },
                        {
                            "id": 3,
                            "title": "Last 24 hours",
                            "type": "graph",
                            "span": 12,
                            "targets": [
                                {
                                    "expr": "event_throughput{time_window='24h'}",
                                    "legendFormat": "{{job}}",
                                    "refId": "C"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
