import io
import os
import unittest
import subprocess
import sys


class TestHiker(unittest.TestCase):
    inputs_and_expected_ouputs = [
        # Empty inputs.
        ('', '0,No'),

        # Troublesome one- and two-letter inputs.
        ('a', '1,No'),
        ('a a ', '2,No'),
        (' a a', '2,No'),
        ('b', '0,No'),
        ('b b ', '0,No'),
        (' b a', '1,No'),

        # Normal words.
        ('happy', '2,No'),
        ('abaaaabaaaba', '4,No'),
        ('happy purple frog', '5,No'),

        # Extra whitespace.
        ('         happy', '2,No'),
        ('happy         ', '2,No'),
        ('\t\t happy\r\n', '2,No'),

        # Different number of lines.
        ('happy / happy', '2,2,No'),
        ('happy / happy / happy', '2,2,2,No'),
        ('happy / happy / happy / happy', '2,2,2,2,No'),
        ('happy / happy / happy / happy / happy', '2,2,2,2,2,No'),

        # Example provided by the spec.
        ('happy purple frog/eating bugs in the marshes/get indigestion', '5,7,5,Yes'),
        ('computer programs/the bugs try to eat my code/i will not let them', '5,8,5,No'),

        # Custom haikus.
        ('lame clean code/complex makes me happy/sorry debugger', '5,7,5,Yes'),
        ('input needs a tty/i will not give it one/what an outrage', '5,8,5,No'),
        ("it's almost perfect/just one line to go/imports galore", '5,7,5,Yes'),
    ]

    def test_hiker(self):
        cmd = [sys.executable, os.path.join('src', 'hiker.py')]

        for input_, expected_output in self.inputs_and_expected_ouputs:
            input_ = bytes(input_ + os.linesep, encoding='utf8')
            output = subprocess.check_output(cmd, input=input_).decode('utf8').strip()
            self.assertEqual(output, expected_output, msg=f'input = {input_}')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
