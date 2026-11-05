import json
import subprocess
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / 'skills' / 'natural-writing-kr'
SCRIPT = SKILL / 'scripts' / 'audit_korean_text.py'

class AuditTests(unittest.TestCase):
    def run_audit(self, *args, input_text=''):
        return subprocess.run([sys.executable, str(SCRIPT), *args], input=input_text, text=True, capture_output=True, cwd=tempfile.gettempdir())

    def test_clean_text_is_not_claimed_to_be_human(self):
        result = self.run_audit(input_text='설정에서 알림을 끌 수 있어요.')
        self.assertEqual(result.returncode, 0)
        self.assertIn('No configured patterns found', result.stdout)

    def test_natural_passive_is_signal_not_default_failure(self):
        result = self.run_audit('--json', input_text='결제 내역이 제공됩니다.')
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        rule = next(item for item in data['findings'] if item['code'] == 'passive-chain')
        self.assertIn('context', rule['advice'])

    def test_strict_flag_is_explicit(self):
        result = self.run_audit('--fail-on-findings', input_text='결제 내역이 제공됩니다.')
        self.assertEqual(result.returncode, 1)

    def test_examples_resolve_from_another_directory(self):
        result = self.run_audit('--after-examples', '--json')
        self.assertEqual(result.returncode, 0, result.stderr)
        examples = json.loads(result.stdout)['examples']
        self.assertEqual(len(examples), 6)
        self.assertTrue(all(Path(x['path']).is_file() for x in examples))

    def test_missing_examples_are_reported_as_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / 'scripts' / SCRIPT.name
            script.parent.mkdir()
            shutil.copyfile(SCRIPT, script)
            result = subprocess.run([sys.executable, str(script), '--after-examples', '--json'], text=True, capture_output=True)
            self.assertEqual(result.returncode, 1)
            examples = json.loads(result.stdout)['examples']
            self.assertTrue(all(x['findings'][0]['code'] == 'missing-after-example' for x in examples))

    def test_missing_input_is_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = self.run_audit(str(Path(tmp) / 'missing-input.md'))
            self.assertNotEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()
