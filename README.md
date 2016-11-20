# Monz
[![PyPI version](https://img.shields.io/pypi/v/monz.svg)][pypi]
[![Python versions](https://img.shields.io/pypi/pyversions/monz.svg)][pypi]
[![License](https://img.shields.io/github/license/pawelad/monz.svg)][license]

[![Build status](https://img.shields.io/travis/pawelad/monz.svg)][travis]
[![Test coverage](https://img.shields.io/coveralls/pawelad/monz.svg)][coveralls]

Simple command line interface for quickly accessing your Monzo account info,
current balance, latest transactions, etc.

I don't know exactly where will this project go next so all feature requests
and suggestions are more then welcome.

Worth mentioning - it currently suffers from the same issue that the underlying
[pymonzo][pymonzo] package suffers, which is the short lifespan of access
tokens. It makes using it daily a bit of a hassle as you need to change it
every couple of hours, but I plan to fix in the near future.

## Installation
From PyPI:
```
$ pip install monz
```

## Usage
To use the script you have to provide it with you Monzo
[access token][monzo developer playground]. You can either do that by exporting
it as an environment variable (`$ export MONZO_ACCESS_TOKEN='...'`) or by
passing it explicitly with each command.

```
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
You can view your linked accounts:
```
$ monz accounts    
Account #1, Bender Rodríguez
ID:          acc_2716057
Created:     Dec 31, 2999 11:59 PM
```

If you have only one then it will become the default one, but if you have more
then you have to pass it's ID explicitly to the rest of the commands.

You can view your current balance, which is also the default subcommand:
```
$ monz       
Balance:     £17.29
Spent today: £0.00

$ monz balance
Balance:     £17.29
Spent today: £0.00
```

Lastly, you can see your latest transactions:
```
$ monz transactions -n 2
-£50.00 at Robot Arms Apartments (New New York)
Category:    Bills
Date:        Nov 18, 3016 11:09 PM

-£50.00 at Fronty's Meat Market (New New York)
Category:    Grocieries
Date:        Nov 17, 3016 8:31 AM
```

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
[pymonzo]: https://github.com/pawelad/pymonzo
[travis]: https://travis-ci.org/pawelad/monz
