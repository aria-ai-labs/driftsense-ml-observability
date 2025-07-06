from driftsense.sdk import monitor

def test_monitor_runs():
    monitor(0.5, {"age":0.03})