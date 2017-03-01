#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import subprocess


# TODO: remove this and its call in plugin_loaded() after a few updates
def temporary_settings_fix():
    s = sublime.load_settings('gpg.sublime-settings')
    if s.has('gpg_command'):
        s.set('gpg.command', s.get('gpg_command', 'gpg'))
        s.erase('gpg_command')
    if s.has('homedir'):
        s.set('gpg.homedir', s.get('homedir', ''))
        s.erase('homedir')
    if s.has('verbosity'):
        s.set('gpg.verbosity', s.get('verbosity', 1))
        s.erase('verbosity')
    if s.has('recipients'):
        s.set('gpg.recipients', s.get('recipients', ''))
        s.erase('recipients')
    if s.has('first_run'):
        s.set('gpg.readme_shown', not s.get('first_run', True))
        s.erase('first_run')
    sublime.save_settings('gpg.sublime-settings')


def plugin_loaded():
    '''
        Sublime 3 calls this once the plugin API is ready.
    '''

    # TODO: remove this fix and its def above after a few updates
    temporary_settings_fix()

    s = sublime.load_settings('gpg.sublime-settings')

    gpg_readme_shown = s.get('gpg.readme_shown', False)
    if not gpg_readme_shown:
        s.set('gpg.readme_shown', True)
        sublime.save_settings('gpg.sublime-settings')
        sublime.set_timeout_async(lambda: sublime.active_window().run_command('gpg_readme'), 5000)



def gpg(view, data, opts_in):
    '''
        gpg calls the gpg binary to process the data and returns the result.
    '''

    window = view.window()
    s = sublime.load_settings('gpg.sublime-settings')
    gpg_command = s.get('gpg.command', 'gpg')
    opts = [gpg_command,
            '--armor',
            '--batch',
            '--no-greeting',
            '--trust-model', 'always',
            '--yes']
    gpg_homedir = s.get('gpg.homedir', '')
    if gpg_homedir:
        opts += ['--homedir', gpg_homedir]
    gpg_log_file = s.get('gpg.log_file', '')
    if gpg_log_file:
        opts += ['--log_file', gpg_log_file]
    for _ in range(0, s.get('gpg.verbosity', 1)):
        opts.append('--verbose')
    opts += opts_in
    try:
        gpg_process = subprocess.Popen(opts,
                                       universal_newlines=False,
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
        result, error = gpg_process.communicate(input=data.encode())
        if error:
            panel(window, error.decode())
        if gpg_process.returncode:
            return None
        return result.decode().strip('\n')
    except IOError as e:
        panel(window, 'Error: %s' % e)
        return None
    except OSError as e:
        panel(window, 'Error: %s' % e)
        return None


def panel(window, message):
    '''
        Panel displays gpg's stderr at the bottom of the window.
    '''

    p = window.create_output_panel('gpg_message')
    p.run_command('gpg_message', {'message': message})
    p.show(p.size())
    window.run_command('show_panel', {'panel': 'output.gpg_message'})


class GpgReadmeCommand(sublime_plugin.TextCommand):
    '''
        Readme
    '''

    def run(self, edit):
        v = self.view.window().new_file()
        v.set_name('GPG: Readme')
        v.settings().set('gutter', False)
        v.insert(edit, 0, sublime.load_resource('Packages/GPG/README.md'))
        v.set_syntax_file('Packages/Markdown/Markdown.sublime-syntax')
        v.set_read_only(True)
        v.set_scratch(True)


class GpgChangelogCommand(sublime_plugin.TextCommand):
    '''
        Changelog
    '''

    def run(self, edit):
        v = self.view.window().new_file()
        v.set_name('GPG: Changelog')
        v.settings().set('gutter', False)
        v.insert(edit, 0, sublime.load_resource('Packages/GPG/CHANGELOG.md'))
        v.set_syntax_file('Packages/Markdown/Markdown.sublime-syntax')
        v.set_read_only(True)
        v.set_scratch(True)


class GpgMessageCommand(sublime_plugin.TextCommand):
    '''
        A helper command for panel.
    '''

    def run(self, edit, message):
        v = self.view
        v.insert(edit, v.size(), message)


class GpgCommand(sublime_plugin.TextCommand):
    '''
        A helper command to replace all selections of the current document's
        content with new content.
    '''

    def run(self, edit, opts):
        v = self.view
        # doc = sublime.Region(0, v.size())
        for selection in v.sel():
            data = gpg(v, v.substr(selection), opts)
            if data:
                # v.replace(edit, doc, data)
                v.replace(edit, selection, data)
