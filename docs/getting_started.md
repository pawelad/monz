# Getting Started
Before starting, please take note of these warnings from [Monzo API docs]:

!!! warning "The Monzo Developer API is not suitable for building public applications"

    You may only connect to your own account or those of a small set of users you
    explicitly allow. Please read our [blog post](https://monzo.com/blog/2017/05/11/api-update/)
    for more detail.

!!! warning "Strong Customer Authentication"

    After a user has authenticated, your client can fetch all of their transactions,
    and after 5 minutes, it can only sync the last 90 days of transactions. If you
    need the user’s entire transaction history, you should consider fetching and
    storing it right after authentication.

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

## Authentication
Before you can access your Monzo account details through `monz`, you need to
authenticate it. You can do that with a (temporary) access token (for example, from
the [Monzo Developer Portal]), or go through a one time OAuth setup that will save
the token on disk and automatically refresh it when it expires.

To do the latter, you should first create an OAuth client in [Monzo developer tools]
(with the "Redirect URL" set to `http://localhost:6600/monz`). If you want the access
token refresh automatically, you need to set the client as confidential. After that,
run the `monz authorize` command with the obtained client ID and client secret.

This should open a new web browser tab (if it didn't, go to the link from the
log message) that will let you authorize the OAuth client you just created. If
everything goes well, you should be redirected to `http://localhost:6600/monz`
and greeted with `Monzo OAuth authorization complete.` message.

Note that you might need to open your mobile app to allow full access to your account.

That's it! The access token is saved locally at `~/.pymonzo` and - as long as you set
the OAuth client as confidential - should be refreshed automatically when it expires.

## Usage
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


[monzo api docs]: https://docs.monzo.com/
[monzo developer portal]: https://developers.monzo.com/
[monzo developer tools]: https://developers.monzo.com/
[pipx]: https://github.com/pypa/pipx
[pypi]: https://pypi.org/
[virtualenv]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
