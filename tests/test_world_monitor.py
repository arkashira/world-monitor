import pytest
from datetime import datetime, timedelta
from src.world_monitor import WorldMonitor, Event

def test_add_event():
    monitor = WorldMonitor()
    event = Event(datetime.now(), "tag1", "region1")
    monitor.add_event(event)
    assert len(monitor.events) == 1

def test_get_event_throughput():
    monitor = WorldMonitor()
    event1 = Event(datetime.now(), "tag1", "region1")
    event2 = Event(datetime.now() - timedelta(minutes=10), "tag1", "region1")
    monitor.add_event(event1)
    monitor.add_event(event2)
    assert monitor.get_event_throughput(timedelta(minutes=5)) == 1

def test_get_events_by_tag():
    monitor = WorldMonitor()
    event1 = Event(datetime.now(), "tag1", "region1")
    event2 = Event(datetime.now(), "tag2", "region1")
    monitor.add_event(event1)
    monitor.add_event(event2)
    assert len(monitor.get_events_by_tag("tag1")) == 1

def test_get_events_by_region():
    monitor = WorldMonitor()
    event1 = Event(datetime.now(), "tag1", "region1")
    event2 = Event(datetime.now(), "tag1", "region2")
    monitor.add_event(event1)
    monitor.add_event(event2)
    assert len(monitor.get_events_by_region("region1")) == 1

def test_get_grafana_dashboard_template():
    monitor = WorldMonitor()
    template = monitor.get_grafana_dashboard_template()
    assert "rows" in template
    assert len(template["rows"]) == 1
    assert "panels" in template["rows"][0]
    assert len(template["rows"][0]["panels"]) == 3
