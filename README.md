# Monz
[![Build status](https://img.shields.io/travis/pawelad/monz.svg)][travis]
[![Test coverage](https://img.shields.io/coveralls/pawelad/monz.svg)][coveralls]
[![PyPI version](https://img.shields.io/pypi/v/monz.svg)][pypi]
[![Python versions](https://img.shields.io/pypi/pyversions/monz.svg)][pypi]
[![License](https://img.shields.io/github/license/pawelad/monz.svg)][license]

Simple (and awesome) command line interface for quickly accessing your
(equally awesome) Monzo account info, its current balance, latest transactions,
etc.

It uses [pymonzo][pymonzo] and its authentication system in the background so
you should to read the [auth section][pymonzo auth section] there first.

## Installation
From PyPI:
```
$ pip install monz
```

## Usage
First, you need to authenticate either via an
[access token][pymonzo access token] or [OAuth 2][pymonzo oauth2].

Everything else should be pretty straightforward:
```
$ monz --help 
Usage: monz [OPTIONS] COMMAND [ARGS]...

  Simple command line interface for quickly accessing your Monzo account
  info, current balance, latest transactions, etc.

  See https://github.com/pawelad/monz for more info.

Options:
  -t, --access-token TEXT  Monzo API access token.
  --help                   Show this message and exit.

Commands:
  accounts      Show connected Monzo accounts
  balance       Show Monzo account balance
  transactions  Show Monzo account transactions
```

## Examples
You can view your linked accounts:
```
$ monz accounts    
Account #1, Bender Rodríguez
ID:          acc_2716057
Created:     Dec 31, 2999 11:59 PM
```

If you have only one then it will become the default one, but if you have more
then you have to pass its ID explicitly to other subcommands.

You can view your current balance, which is also the default subcommand:
```
$ monz balance
Balance:     £17.29
Spent today: £0.00

$ monz       
Balance:     £17.29
Spent today: £0.00
```

Lastly, you can see your latest transactions:
```
$ monz transactions -n 2
-£50.00 | Robot Arms Apartments (New New York)
Category:    Bills
Date:        Nov 18, 3016 11:09 PM

-£9.20 | Fronty's Meat Market (New New York)
Category:    Grocieries
Date:        Nov 17, 3016 8:31 AM
```

## Tests
Package was tested with the help of `py.test` and `tox` on Python 2.7, 3.4, 3.5
and 3.6 (see `tox.ini`).

Code coverage is available at [Coveralls][coveralls].

To run tests yourself you need to set environment variables with access token
before running `tox` inside the repository:
```shell
$ pip install requirements/dev.txt
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
[monzo]: https://monzo.com/
[monzo api playground]: https://developers.getmondo.co.uk/api/playground
[pawelad]: https://github.com/pawelad
[pymonzo]: https://github.com/pawelad/pymonzo
[pymonzo access token]: https://github.com/pawelad/pymonzo#access-token
[pymonzo auth section]: https://github.com/pawelad/pymonzo#authentication
[pymonzo oauth2]: https://github.com/pawelad/pymonzo#oauth-2
[pypi]: https://pypi.python.org/pypi/monz
[travis]: https://travis-ci.org/pawelad/monz
