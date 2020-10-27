import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_delete import gits_delete
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(branch='branch_name', count=2))
@patch("subprocess.Popen")
def test_gits_delete_happy_case(mock_var, mock_args):
    """
    Function to test gits delete, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_delete(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("gits_logging.gits_logger")
def test_gits_delete_sad_case(mock_err, mock_args):
    """
    Function to test gits delete, failure case
    """
    mock_args = parse_args(mock_args)
    test_result = gits_delete(mock_args)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
