from layers.L2.behavioral_analyzer import BehavioralAnalyzer

def test_behavioral_analysis():
    analyzer = BehavioralAnalyzer()
    for port in [22, 22, 80]:
        result = analyzer.analyze({"src_ip": "1.1.1.1", "dest_port": port})
    assert result["unique_ports"] == 2
    assert result["total_events"] == 3
