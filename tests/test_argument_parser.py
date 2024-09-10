import pytest
from commandhelper.argument_parser import Parser
from commandhelper.const import ARGUMENT_PLACEHOLDER


def _args(**override):
    args = {'alias': None, 'command': [], 'yes': False,
            'help': False, 'version': False, 'debug': False,
            'force_command': None, 'repeat': False,
            'enable_experimental_instant_mode': False,
            'shell_logger': None}
    args.update(override)
    return args


@pytest.mark.parametrize('argv, result', [
    (['commandhelper'], _args()),
    (['commandhelper', '-a'], _args(alias='alo')),
    (['commandhelper', '--alias', '--enable-experimental-instant-mode'],
     _args(alias='alo', enable_experimental_instant_mode=True)),
    (['commandhelper', '-a', 'fix'], _args(alias='fix')),
    (['commandhelper', 'git', 'branch', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch'], yes=True)),
    (['commandhelper', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch', '-a'], yes=True)),
    (['commandhelper', ARGUMENT_PLACEHOLDER, '-v'], _args(version=True)),
    (['commandhelper', ARGUMENT_PLACEHOLDER, '--help'], _args(help=True)),
    (['commandhelper', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y', '-d'],
     _args(command=['git', 'branch', '-a'], yes=True, debug=True)),
    (['commandhelper', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-r', '-d'],
     _args(command=['git', 'branch', '-a'], repeat=True, debug=True)),
    (['commandhelper', '-l', '/tmp/log'], _args(shell_logger='/tmp/log')),
    (['commandhelper', '--shell-logger', '/tmp/log'],
     _args(shell_logger='/tmp/log'))])
def test_parse(argv, result):
    assert vars(Parser().parse(argv)) == result
