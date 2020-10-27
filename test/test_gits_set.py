import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_set import gits_set_func
from mock import patch, Mock, mock_open


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(parent="parent"))
@patch("subprocess.Popen")
@patch("pathlib.Path.home", return_value="home directory")
@patch("os.path.join", return_value="parent file")
@patch("builtins.open", create=True)
@patch("gits_logging.gits_logger")
def test_gits_set_happy_case(mock_logger, mock_file, mock_parent_file, mock_home, mock_var, mock_args):
    """
    Function to test gits set, success case
    """
    mocked_pipe1 = Mock()
    attrs1 = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe1.configure_mock(**attrs1)
    mock_var.return_value = mocked_pipe1

    mock_file.return_value = mock_open(read_data="Data1").return_value

    mock_args = parse_args(mock_args)
    test_result = gits_set_func(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(parent=None))
@patch("gits_logging.gits_logger")
def test_gits_set_sad_case_invalid_parent(mock_logger, mock_args):
    """
    Function to test gits set, failure case when parent is not valid
    """
    mock_args = parse_args(mock_args)
    test_result = gits_set_func(mock_args)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
def test_gits_set_sad_case_no_arguments(mock_args):
    """
    Function to test gits set, failure case when no arguments are passed
    """
    mock_args = parse_args(mock_args)
    test_result = gits_set_func(mock_args)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
