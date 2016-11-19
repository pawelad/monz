# Monz
[![PyPI version](https://img.shields.io/pypi/v/monz.svg)][pypi]
[![Python versions](https://img.shields.io/pypi/pyversions/monz.svg)][pypi]
[![License](https://img.shields.io/github/license/pawelad/monz.svg)][license]

[![Build status](https://img.shields.io/travis/pawelad/monz.svg)][travis]
[![Test coverage](https://img.shields.io/coveralls/pawelad/monz.svg)][coveralls]

Simple command line interface for quickly accessing your Monzo account info,
current balance, latest transactions, etc.

It currently suffers from the same issue that the underlying [pymonzo][pymonzo]
suffers - short lifespan of access tokens.

## Installation
From PyPI:
```shell
$ pip install monzo
```

## Usage
To use the library you have to provide it with you Monzo
[access token][monzo developer playground]. You can either do that by exporting
it as an environment variable (`$ export MONZO_ACCESS_TOKEN='...'`) or by
passing it explicitly with each command.

```shell
$ monz --help 
Usage: monz [OPTIONS] COMMAND [ARGS]...

  Simple command line interface for quickly accessing your Monzo account
  info, current balance, latest transactions, etc.

  To use it you need to save your Monzo access token as 'MONZO_ACCESS_TOKEN'
  environment variable (export MOZNO_ACCESS_TOKEN='...') or pass it
  explicitly with each command.

Options:
  -t, --access-token TEXT  Monzo API access token.
  --help                   Show this message and exit.

Commands:
  accounts      Show connected Monzo accounts
  balance       Show Monzo account balance
  transactions  Show Monzo account transactions
```

## Examples


## Tests
Package was tested with the help of `py.test` and `tox` on Python 2.7, 3.4
and 3.5 (see `tox.ini`).

To run tests yourself you need to set environment variables with access token
before running `tox` inside the repository:
```shell
$ export MONZO_ACCESS_TOKEN='...'
$ tox
```

## Contributions
Package source code is available at [GitHub][github].

Feel free to use, ask, fork, star, report bugs, fix them, suggest enhancements,
add functionality and point out any mistakes.

## Authors
Developed and maintained by [Paweł Adamczak][pawelad].

Released under [MIT License][license].


[coveralls]: https://coveralls.io/github/pawelad/monz
[github add issue]: https://github.com/pawelad/monz/issues/new
[github]: https://github.com/pawelad/monz
[license]: https://github.com/pawelad/monz/blob/master/LICENSE
[monzo developer playground]: https://developers.getmondo.co.uk/api/playground
[monzo]: https://monzo.com/
[pawelad]: https://github.com/pawelad
[pypi]: https://pypi.python.org/pypi/monz
[travis]: https://travis-ci.org/pawelad/monz
