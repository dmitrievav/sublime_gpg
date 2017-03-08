# GPG plugin for [Sublime Text](https://www.sublimetext.com)

[![License](https://img.shields.io/github/license/dmitrievav/sublime_gpg.svg?style=flat-square)](https://github.com/dmitrievav/sublime_gpg/blob/master/LICENSE)
[![Downloads Package Control](https://img.shields.io/packagecontrol/dt/GPG.svg?style=flat-square)](https://packagecontrol.io/packages/GPG)
[![Latest release](https://img.shields.io/github/release/dmitrievav/sublime_gpg.svg?style=flat-square)](https://github.com/dmitrievav/sublime_gpg/releases/latest)

> A reincarnation of <https://github.com/crowsonkb/SublimeGPG>, which was closed by its author due security risks. In few words, you should switch off auto updates and check all source code of software you use, otherwise you have to blame only yourself.

## Requirements

This plug-in targets and is tested against the **latest Build** of Sublime Text.

* [ST3 (stable)](https://www.sublimetext.com/3)
* [ST3 (dev)](https://www.sublimetext.com/3dev)

This plugin adds commands to decrypt, encrypt, sign, and authenticate documents. It requires a working copy of [GPG](http://www.gnupg.org/) with a key already generated. (If you haven't generated a key yet, see [this mini-HOWTO](http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto-3.html#ss3.1).) If the gpg binary is not in your `$PATH`, you will have to set its location in Preferences → Package Settings → GPG.

On OS X, I recommend installing GPG using the [Homebrew package manager](http://brew.sh/): after installing Homebrew, run `brew install gpg`.

![sublime_gpg](https://dmitrievav.github.io/gifs/sublime_gpg.gif "sublime_gpg")

## Installation

Using **Package Control** is not required, but recommended as it keeps your packages (with their dependencies) up-to-date!

### Installation via Package Control

* [Install Package Control](https://packagecontrol.io/installation#st3)
  * Close and reopen Sublime Text after having installed Package Control.
* Open the Command Palette (`Tools > Command Palette`).
* Choose `Package Control: Install Package`.
* Search for [`GPG` on Package Control](https://packagecontrol.io/packages/GPG) and select to install.

In case if this plugin is not available with default `Package Control` channel, you can add repository manually by `Package Control: Add Repository`

<https://raw.githubusercontent.com/dmitrievav/sublime_gpg/master/repository.json>

### Manual installation

Download the zip file from the [latest release page](https://github.com/dmitrievav/sublime_gpg/releases/latest) and unpack its contents to a subfolder named `GPG` in `../Sublime Text 3/Data/Packages` where Sublime Text 3 is installed.

## Usage

The plug-in's actions are available via the main menu (`Tools → GPG`) or the Command Palette (`GPG: ...`).

### Key bindings

The two main actions of the plug-in are also assigned the following default key bindings:

* Decrypt: "super+g,d"
* Encrypt: "super+g,e"

## Flaws and limitations

- Signatures can only be created with the default key (the first key in the secret key ring, or else the default specified in `gpg.conf`).

## Settings

You can use the main menu or the Command Palette to customize the GPG plug-in's preferences.

## Source code

[github.com/dmitrievav/sublime_gpg](https://github.com/dmitrievav/sublime_gpg)
