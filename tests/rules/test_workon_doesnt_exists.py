import pytest
from commandhelper.rules.workon_doesnt_exists import match, get_new_command
from commandhelper.types import Command


@pytest.fixture(autouse=True)
def envs(mocker):
    return mocker.patch(
        'commandhelper.rules.workon_doesnt_exists._get_all_environments',
        return_value=['commandhelper', 'code_view'])


@pytest.mark.parametrize('script', [
    'workon tehalo', 'workon code-view', 'workon new-env'])
def test_match(script):
    assert match(Command(script, ''))


@pytest.mark.parametrize('script', [
    'workon commandhelper', 'workon code_view', 'work on tehalo'])
def test_not_match(script):
    assert not match(Command(script, ''))


@pytest.mark.parametrize('script, result', [
    ('workon tehalo', 'workon commandhelper'),
    ('workon code-view', 'workon code_view'),
    ('workon zzzz', 'mkvirtualenv zzzz')])
def test_get_new_command(script, result):
    assert get_new_command(Command(script, ''))[0] == result
