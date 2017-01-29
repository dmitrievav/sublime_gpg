import sublime
import sublime_plugin

import subprocess
import re

PIPE = subprocess.PIPE


def plugin_loaded():
  """Sublime 3 calls this once the plugin API is ready."""

  print('GPG: plugin is loaded.')
  sublime.set_timeout_async(lambda: sublime.active_window().run_command('gpg_help_once'), 5000)


def gpg(view, data, opts_in):
  """gpg calls the gpg binary to process the data and returns the result."""

  window = view.window()
  s = sublime.load_settings('gpg.sublime-settings')
  gpg_command = s.get('gpg_command')
  opts = [gpg_command,
          '--armor',
          '--batch',
          '--trust-model', 'always',
          '--yes']
  homedir = s.get('homedir')
  if homedir:
    opts += ['--homedir', homedir]
  for _ in range(0, s.get('verbosity')):
    opts.append('--verbose')
  opts += opts_in
  try:
    gpg_process = subprocess.Popen(opts, universal_newlines=False,
                                   stdin=PIPE, stdout=PIPE, stderr=PIPE)
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
  """panel displays gpg's stderr at the bottom of the window."""

  p = window.create_output_panel('gpg_message')
  p.run_command('gpg_message', {'message': message})
  p.show(p.size())
  window.run_command('show_panel', {'panel': 'output.gpg_message'})


def get_recipients(window, on_done):
  s = sublime.load_settings('gpg.sublime-settings')
  window.show_input_panel('Recipients:', s.get('recipients'), lambda recipient: on_done(recipient), None, None)


def format_recipients(recipients):
  opts = []
  recipients = re.split(';|,| ', recipients)
  for recipient in recipients:
    recipient = recipient.strip(' \t\n\r')
    if recipient:
      opts.append("--recipient")
      opts.append(recipient)
  return opts


class GpgHelpCommand(sublime_plugin.TextCommand):
  """Help."""

  def run(self, edit):
    window = self.view.window()
    window.run_command('open_file', {"file": "${packages}/GPG/README.md"})


class GpgHelpOnceCommand(sublime_plugin.TextCommand):
  """Show help once."""

  def run(self, edit):
    s = sublime.load_settings('gpg.sublime-settings')
    first_run = s.get('first_run')
    if first_run:
      s.set('first_run', False)
      sublime.save_settings('gpg.sublime-settings')
      window = self.view.window()
      window.run_command('gpg_help')


class GpgMessageCommand(sublime_plugin.TextCommand):
  """A helper command for panel."""

  def run(self, edit, message):
    self.view.insert(edit, self.view.size(), message)


class GpgCommand(sublime_plugin.TextCommand):
  """A helper command to replace the document content with new content."""

  def run(self, edit, opts):
    # doc = sublime.Region(0, self.view.size())
    data = gpg(self.view, self.view.substr(self.view.sel()[0]), opts)
    if data:
      # self.view.replace(edit, doc, data)
      self.view.replace(edit, self.view.sel()[0], data)


class GpgDecryptCommand(sublime_plugin.WindowCommand):
  """Decrypts an OpenPGP format message."""

  def run(self):
    opts = []
    self.window.active_view().run_command('gpg', {'opts': opts})


class GpgEncryptCommand(sublime_plugin.WindowCommand):
  """Encrypts plaintext to an OpenPGP format message."""

  def run(self):
    get_recipients(self.window, self.on_done)

  def on_done(self, recipients):
    opts = ['--encrypt'] + format_recipients(recipients)
    self.window.active_view().run_command('gpg', {'opts': opts})


class GpgSignCommand(sublime_plugin.WindowCommand):
  """Signs the document using a clear text signature."""

  def run(self):
    opts = ['--clearsign']
    self.window.active_view().run_command('gpg', {'opts': opts})


class GpgSignAndEncryptCommand(sublime_plugin.WindowCommand):
  """Encrypts plaintext to a signed OpenPGP format message."""

  def run(self):
    get_recipients(self.window, self.on_done)

  def on_done(self, recipients):
    opts = ['--sign',
            '--encrypt'
            ] + format_recipients(recipients)
    self.window.active_view().run_command('gpg', {'opts': opts})


class GpgVerifyCommand(sublime_plugin.WindowCommand):
  """Verifies the document's signature without altering the document."""

  def run(self):
    opts = ['--verify']
    self.window.active_view().run_command('gpg', {'opts': opts})
