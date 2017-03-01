## GPG plugin for Sublime Text 3

### CHANGES in `3.0.4`

* updated `README.md`
  * fixed sections
  * moved setting descriptions to comments in default settings file
  * added shields badges
* added `CHANGELOG.md`
* added `.github/ISSUE_TEMPLATE.md`
* modular approach to package
  * Python source code
    * 4 spaces indentation
    * added Package Control events notifier
    * split up `gpg.py` into:
      * `src/text_commands.py`
      * `src/window_commands.py`
    * open `README.md` and `CHANGELOG.md` as read_only, scratch copy in new tab
  * fix commands
    * 4 spaces indentation
    * settings and key bindings should be listed under `Preferences: GPG: ...`
  * fix settings
    * 4 spaces indentation
    * changed naming scheme
    * added python code for transition period
    * added optional `log_file` option
    * show settings side-by-side like sublime
  * fix key bindings
    * 4 spaces indentation
    * move into `input-maps` subfolder
    * show key bindings side-by-side like sublime
      * needed to split into platform specific files
  * fix menus
    * 4 spaces indentation
    * fix international menus by targetting sublime menu items by id only
    * remove readme option from context menu and tools
    * rename Help options to Readme
* added `.gitignore`
* fixed messages
  * 4 spaces indentation
  * readability++ in `messages/install.md`
  * added `messages/latest.md`
    * reference it in `messages.json`

### Feedback

Right-click and open the following link:

* <https://github.com/dmitrievav/sublime_gpg>
