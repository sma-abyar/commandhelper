import pytest
from commandhelper.rules.java import match, get_new_command
from commandhelper.types import Command


@pytest.mark.parametrize('command', [
    Command('java foo.java', ''),
    Command('java bar.java', '')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('java foo.java', ''), 'java foo'),
    (Command('java bar.java', ''), 'java bar')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
