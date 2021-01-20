import unittest

from click.testing import CliRunner
from packages.python.hello.cli import cli


class TestCompute(unittest.TestCase):
    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli.hello, ["--name=Peter"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, "Hello Peter\n")


if __name__ == "__main__":
    unittest.main()
