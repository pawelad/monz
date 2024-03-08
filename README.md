# monz
[![Package Version](https://img.shields.io/pypi/v/monz)][pypi monz]
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/monz)][pypi monz]
[![Read the Docs](https://img.shields.io/readthedocs/monz)][rtfd monz]
[![Codecov](https://img.shields.io/codecov/c/github/pawelad/monz)][codecov monz]
[![License](https://img.shields.io/pypi/l/monz)][license]
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]
[![py.typed](https://img.shields.io/badge/py-typed-FFD43B)][rickroll]

Simple CLI for your Monzo account.

## Installation
Since `monz` is a command line tool, the recommended installation method is via [pipx]:

```console
$ pipx install monz
```

Of course, you can just install it directly from [PyPI] (ideally, inside a
[virtualenv]):

```console
$ python -m pip install monz
```

## Quick start

### Authentication
Before you can access your Monzo account details through `monz`, you need to
authenticate it. You can do that with a (temporary) access token (for example, from
the [Monzo Developer Portal]), or go through a one time OAuth setup that will save
the  token on disk and automatically refresh it when it expires.

To do the latter, you should first create an OAuth client in Monzo developer tools
(with the "Redirect URL" set to `http://localhost:6600/monz`) and run the
`monz authorize` command with obtained client ID and client secret.

For more information, please take a look at:
https://pymonzo.pawelad.dev/en/latest/getting_started/#authentication

### Usage
The default subcommand is `info`, which shows your account balance and its
latest transaction:

```console
$ monz
Balance:                 £203.78
Total balance:           £303.78
Currency:                GBP
Spend today:             £4.20
Local currency:          THB
Local exchange rate:     45.558219

Last transaction:
         -£17.29 | MomCorp
ID:              tx_0000Lxo9IgPERj43i03iKH
Description:     MomCorp
Amount:          -£17.29
Currency:        GBP
Category:        general
Notes:           ✨                       
Created:         Feb 12, 3024, 12:39:22 PM
Settled:         Feb 13, 3024, 1:36:48 AM
```

You can view all linked accounts:

```console
$ monz accounts
   Account 'acc_87539319' (GB)   
ID:                 acc_87539319
Description:        user_1729
Currency:           GBP
Account Number:     0101100101   
Sort Code:          04-00-04                   
Type:               uk_retail                  
Closed:             No                         
Created:            Dec 31, 2999, 11:59:59 PM  
```

If you have only one (active) account, it will be used everywhere by default.
If you have more, you'll have to pass its ID explicitly when needed via the
`--account_id` option.

Finally, you can see your latest transactions:

```
$ monz transactions -n 2 
         -£17.29 | MomCorp
ID:              tx_0000Lxo9IgPERj43i03iKH
Description:     MomCorp
Amount:          -£17.29
Currency:        GBP
Category:        general
Notes:           ✨                       
Created:         Feb 12, 3024, 12:39:22 PM
Settled:         Feb 13, 3024, 1:36:48 AM

   -£100.00 | pot_0000aDhHH8z3jvram0L0Di   
ID:              tx_0000FskkLc0KB7aK0SV4cd
Description:     pot_0000aDhHH8z3jvram0L0Di
Amount:          -£100.00
Currency:        GBP
Category:        savings
Created:         Feb 6, 3024, 10:49:22 AM
Settled:         Feb 6, 3024, 10:49:22 AM
```

You can see all available subcommands and options by running `monz --help` (or adding
`--help` to any subcommand).

## Authors
Developed and maintained by [Paweł Adamczak][pawelad].

Source code is available at [GitHub][github monz].

Released under [Mozilla Public License 2.0][license].


[black]: https://github.com/psf/black
[codecov monz]: https://app.codecov.io/github/pawelad/monz
[github monz]: https://github.com/pawelad/monz
[license]: ./LICENSE
[monzo developer portal]:  https://developers.monzo.com/
[pawelad]: https://pawelad.me/
[pipx]: https://github.com/pypa/pipx
[pypi monz]: https://pypi.org/project/monz/
[pypi]: https://pypi.org/
[rickroll]: https://www.youtube.com/watch?v=I6OXjnBIW-4&t=15s
[rtfd monz]: https://monz.rtfd.io/
[virtualenv]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
