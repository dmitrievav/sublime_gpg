#!/usr/bin/env python
# coding: utf-8


PACKAGE_NAME = 'GPG'


def status_msg(msg):
    import sublime
    sublime.status_message(PACKAGE_NAME + ': ' + msg)


def plugin_loaded():
    try:
        from package_control import events
        if events.install(PACKAGE_NAME):
            status_msg('Installed %s' % events.install(PACKAGE_NAME))
        elif events.post_upgrade(PACKAGE_NAME):
            status_msg('Upgraded to %s' % events.post_upgrade(PACKAGE_NAME))
    except Exception as e:
        print(e)


def plugin_unloaded():
    try:
        from package_control import events
        if events.pre_upgrade(PACKAGE_NAME):
            status_msg('Upgrading from %s' % events.pre_upgrade(PACKAGE_NAME))
        elif events.remove(PACKAGE_NAME):
            status_msg('Removing %s' % events.remove(PACKAGE_NAME))
    except Exception as e:
        print(e)
