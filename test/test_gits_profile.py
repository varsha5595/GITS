import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_profile import gits_set_profile
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(email="email@address.com", name="name"))
@patch("subprocess.Popen")
def test_gits_profile_happy_case(mock_var, mock_args):
    """
    Function to test gits profile, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_set_profile(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(email="email", name="name"))
@patch("subprocess.Popen")
def test_gits_profile_sad_case_invalid_email(mock_var, mock_args):
    """
    Function to test gits profile, failure case when email is invalid
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_set_profile(mock_args)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_profile_sad_case_no_arguments(mock_var, mock_args):
    """
    Function to test gits profile, failure case when no arguments are passed
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_set_profile(mock_args)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
