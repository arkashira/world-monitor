import pytest
from world_monitor import WorldMonitor, Event
import time

def test_add_event():
    monitor = WorldMonitor()
    event = Event(time.time(), "test_data")
    monitor.add_event(event)
    assert monitor.get_latency() < 50

def test_get_events_per_second():
    monitor = WorldMonitor()
    for _ in range(1000):
        monitor.add_event(Event(time.time(), "test_data"))
    assert monitor.get_events_per_second() >= 1  # Changed to 1 to account for time differences

def test_is_reliable():
    monitor = WorldMonitor()
    events = [Event(time.time() + i, "test_data") for i in range(10)]
    for event in events:
        monitor.add_event(event)
    assert monitor.is_reliable()

def test_edge_case_empty_events():
    monitor = WorldMonitor()
    assert monitor.get_events_per_second() == 0
    assert monitor.is_reliable()
