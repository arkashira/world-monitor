# World Monitor
A customizable dashboard for monitoring event consumption patterns.

## Features
* Pre-built Grafana dashboard templates for Prometheus metrics
* User-configurable filters by semantic tag and geographic region
* Real-time event throughput visualization (last 5m/1h/24h)

## Usage
1. Install the package using `poetry install`
2. Run the tests using `pytest`
3. Use the `WorldMonitor` class to create a monitor instance and add events
4. Use the `get_event_throughput` method to get the event throughput for a given time window
5. Use the `get_events_by_tag` and `get_events_by_region` methods to filter events by tag and region
6. Use the `get_grafana_dashboard_template` method to get a pre-built Grafana dashboard template
