import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_sync import gits_sync
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(source="branch name"))
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
@patch("helper.get_trunk_branch_name", return_value="main branch")
def test_gits_sync_happy_case_source_branch(mock_main_branch, mock_curr_branch, mock_var, mock_args):
    """
    Function to test gits sync, success case when source branch is given
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_sync(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(source=None))
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
@patch("helper.get_trunk_branch_name", return_value="main branch")
def test_gits_sync_happy_case_no_source_branch(mock_main_branch, mock_curr_branch, mock_var, mock_args):
    """
    Function to test gits sync, success case when source branch is not given
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_sync(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(source="branch name"))
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
@patch("helper.get_trunk_branch_name", return_value="main branch")
def test_gits_sync_sad_case_uncommitted_changes(mock_main_branch, mock_curr_branch, mock_var, mock_args):
    """
    Function to test gits sync, failure case when there are uncommitted changes
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'anything', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_sync(mock_args)
    if not test_result:
        assert True
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
@patch("helper.get_trunk_branch_name", return_value="main branch")
def test_gits_sync_sad_case_no_arguments(mock_main_branch, mock_curr_branch, mock_var, mock_args):
    """
    Function to test gits sync, failure case when no arguments are given
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_sync(mock_args)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
