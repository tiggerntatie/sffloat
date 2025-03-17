import unittest
import os
import sys
from io import StringIO
from sffloat import SFFloat


class TestReadme(unittest.TestCase):
    """
    Execute the code blocks in README.md and verify the ouputs
    """
    def test_readme(self):
        old_stdout = sys.stdout
        with open('README.md') as f:
            lines = f.readlines()
        state = "waitcode"
        code = ""
        output = ""
        readoutput = ""
        for l in lines:
            if state in ["waitcode","waitoutput"] and l.find('```python') == 0:
                code = ""
                state = "readcode"
            elif state == "readcode":
                if l.find('```') == 0:
                    redirected_output = sys.stdout = StringIO()
                    exec(code)
                    output = redirected_output.getvalue()
                    sys.stdout = old_stdout
                    state = "waitoutput"
                else:
                    code += l
            elif state == "waitoutput" and l.find('```') == 0:
                state = "readoutput"
                readoutput = ""
            elif state == "waitoutput":
                state = "waitcode"
            elif state == "readoutput":
                if l.find('```') == 0:
                    state = "waitcode"
                    self.assertEqual(readoutput, output)
                else:
                    readoutput += l

