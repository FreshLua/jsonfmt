import json
import os
import subprocess
import sys


def test_utf8_input_preserved(tmp_path):
    sample = tmp_path / 'u.json'
    sample.write_text('{"k": "h\u00e9llo \u2603"}', encoding='utf-8')
    cli = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'cli.py'))
    proc = subprocess.run(
        [sys.executable, cli, str(sample)],
        capture_output=True, text=True, encoding='utf-8',
        cwd=os.path.dirname(cli),
    )
    assert proc.returncode == 0
    assert json.loads(proc.stdout)['k'] == 'h\u00e9llo \u2603'
