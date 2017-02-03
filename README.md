GPG plugin for Sublime Text 3
=============================

A reincarnation of https://github.com/crowsonkb/SublimeGPG, which was closed by its author due security risks. In few words, you should switch off auto updates and check all source code of software you use, otherwise you have to blame only yourself.

For people who are ready to proceed:

The new home of the plugin is https://github.com/dmitrievav/sublime_gpg

This plugin adds commands to decrypt, encrypt, sign, and authenticate documents. It requires a working copy of [GPG](http://www.gnupg.org/) with a key already generated. (If you haven't generated a key yet, see [this mini-HOWTO](http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto-3.html#ss3.1).) If the gpg binary is not in `$PATH`, you will have to set its location in Preferences → Package Settings → GPG.

On OS X, I recommend installing GPG using the [Homebrew package manager](http://brew.sh/): after installing Homebrew, run `brew install gpg`.

![sublime_gpg](https://dmitrievav.github.io/gifs/sublime_gpg.gif "sublime_gpg")

Install
-------

The best possible way is [`Package Control`](https://packagecontrol.io/installation)

Preferences → Package Control → Install Package, then type GPG.

In case if this plugin is not available with default `Package Control` channel, you can add repository manually by `Package Control: Add Repository`

https://raw.githubusercontent.com/dmitrievav/sublime_gpg/master/repository.json

And the last alternative is just coping this repo into `/Sublime Text 3/Packages` folder.

Menu items
----------

- Preferences → Package Settings → GPG
- Tools → GPG → Decrypt
- Tools → GPG → Encrypt
- Tools → GPG → Sign
- Tools → GPG → Sign and encrypt
- Tools → GPG → Verify signature
- Tools → GPG → Help

Key bindings
----------

- Decrypt: "super+g,d"
- Encrypt: "super+g,e"

Settings
--------

- `gpg_command`: You may need to specify the full path if `gpg` is not in `$PATH`.

    Default: `"gpg"`

- `homedir`: Sets the GPG home directory to something other than `~/.gnupg`. If empty, uses the default home directory.

    Default: `""`

- `verbosity`: Valid values: 0–2.

    Default: `1`

- `recipients`: Default recipients splitted by comma.

    Default: `""`

Flaws and limitations
---------------------

- Signatures can only be created with the default key (the first key in the secret key ring, or else the default specified in `gpg.conf`).
