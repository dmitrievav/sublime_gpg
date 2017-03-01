#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import re


def get_recipients(window, on_done):
    s = sublime.load_settings('gpg.sublime-settings')
    recipients = s.get('gpg.recipients')
    window.show_input_panel('Recipients:',
                            recipients,
                            lambda recipient: on_done(recipient),
                            None,
                            None)


def format_recipients(recipients):
    opts = []
    recipients = re.split(';|,| ',
                          recipients)
    for recipient in recipients:
        recipient = recipient.strip(' \t\n\r')
        if recipient:
            opts.append('--recipient')
            opts.append(recipient)
    return opts


class GpgDecryptCommand(sublime_plugin.WindowCommand):
    '''
        Decrypts an OpenPGP format message.
    '''

    def run(self):
        opts = []
        v = self.window.active_view()
        v.run_command('gpg', {'opts': opts})


class GpgEncryptCommand(sublime_plugin.WindowCommand):
    '''
        Encrypts plaintext to an OpenPGP format message.
    '''

    def run(self):
        get_recipients(self.window, self.on_done)

    def on_done(self, recipients):
        opts = ['--encrypt'] + format_recipients(recipients)
        v = self.window.active_view()
        v.run_command('gpg', {'opts': opts})


class GpgSignCommand(sublime_plugin.WindowCommand):
    '''
        Signs the document using a clear text signature.
    '''

    def run(self):
        opts = ['--clearsign']
        v = self.window.active_view()
        v.run_command('gpg', {'opts': opts})


class GpgSignAndEncryptCommand(sublime_plugin.WindowCommand):
    '''
        Encrypts plaintext to a signed OpenPGP format message.
    '''

    def run(self):
        get_recipients(self.window, self.on_done)

    def on_done(self, recipients):
        opts = ['--sign', '--encrypt'] + format_recipients(recipients)
        v = self.window.active_view()
        v.run_command('gpg', {'opts': opts})


class GpgVerifyCommand(sublime_plugin.WindowCommand):
    '''
        Verifies the document's signature without altering the document.
    '''

    def run(self):
        opts = ['--verify']
        v = self.window.active_view()
        v.run_command('gpg', {'opts': opts})
