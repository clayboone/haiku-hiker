import io
import unittest
from contextlib import redirect_stdout

import hiker


class TestHiker(unittest.TestCase):
    inputs_and_expected_ouputs = [
        # Empty inputs
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

        # Custom haiku.
        ('lame clean code/complex makes me happy/sorry debugger', '5,7,5,Yes'),
    ]

    def test_main(self):
        for input_string, expected_output in self.inputs_and_expected_ouputs:
            my_stdout = io.StringIO()

            with redirect_stdout(my_stdout):
                hiker.main(input_string)
                actual_output = my_stdout.getvalue().rstrip('\n')
                self.assertEqual(actual_output, expected_output, f'input = "{input_string}"')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
