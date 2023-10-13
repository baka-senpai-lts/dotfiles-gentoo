
#import dracula.draw

#import catppuccin

config.set("colors.webpage.darkmode.enabled", True)

# Load existing settings made via :set
config.load_autoconfig()


import subprocess
def read_xresources(prefix):
    props = {}
    x = subprocess.run(['xrdb', '-query'], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split('\n')
    for line in filter(lambda l : l.startswith(prefix), lines):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props
xresources = read_xresources('*')

c.fonts.default_family = 'Tamzen'
c.fonts.default_size = '11pt'

c.colors.statusbar.normal.bg = xresources['*background']
c.colors.completion.fg = xresources['*color4']
c.colors.completion.odd.bg = xresources['*background']
c.colors.completion.even.bg = xresources['*background']
c.colors.completion.category.fg = xresources['*color6']
c.colors.completion.category.bg = xresources['*background']
c.colors.completion.category.border.top = xresources['*color1']
c.colors.completion.category.border.bottom = xresources['*color1']
c.colors.completion.item.selected.fg = xresources['*color0']
c.colors.completion.item.selected.bg = xresources['*color6']
c.colors.completion.item.selected.border.top = xresources['*color4']
c.colors.completion.item.selected.border.bottom = xresources['*color4']
c.colors.completion.item.selected.match.fg = xresources['*color0']
c.colors.completion.match.fg = xresources['*color5']

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = xresources['*color1']

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = xresources['*background']

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = xresources['*background']

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = xresources['*color1']

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = xresources['*background']

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  xresources['*color4']

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = xresources['*background']

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = xresources['*color4']

# Background color for the download bar.
c.colors.downloads.bar.bg = xresources['*background']

# Color gradient start for download text.
c.colors.downloads.start.fg = xresources['*color5']

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = xresources['*background']

# Color gradient end for download text.
c.colors.downloads.stop.fg = xresources['*color4']

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = xresources['*background']


# Foreground color for downloads with errors.
c.colors.downloads.error.fg = xresources['*color2']

# Font color for hints.
c.colors.hints.fg = xresources['*color6']

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = xresources['*background']

# Font color for the matched part of hints.
c.colors.hints.match.fg = xresources['*color4']

# Text color for the keyhint widget.
c.colors.keyhint.fg = xresources['*color4']

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = xresources['*color6']

# Background color of the keyhint widget.
c.colors.keyhint.bg = xresources['*background']

# Foreground color of an error message.
c.colors.messages.error.fg = xresources['*color6']

# Background color of an error message.
c.colors.messages.error.bg = xresources['*background']

# Border color of an error message.
c.colors.messages.error.border = xresources['*color4']

# Foreground color of a warning message.
c.colors.messages.warning.fg = xresources['*color4']

# Background color of a warning message.
c.colors.messages.warning.bg = xresources['*background']

# Border color of a warning message.
c.colors.messages.warning.border = xresources['*color4']

# Foreground color of an info message.
c.colors.messages.info.fg = xresources['*color4']

# Background color of an info message.
c.colors.messages.info.bg = xresources['*background']

# Border color of an info message.
c.colors.messages.info.border = xresources['*color4']

# Foreground color for prompts.
c.colors.prompts.fg = xresources['*color4']

# Border used around UI elements in prompts.
c.colors.prompts.border = xresources['*color4']

# Background color for prompts.
c.colors.prompts.bg = xresources['*background']

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = xresources['*color6']

# Foreground color for the selected item in filename prompts.
c.colors.prompts.selected.fg = xresources['*color0']

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = xresources['*color4']

# Background color of the statusbar.
c.colors.statusbar.normal.bg = xresources['*background']


# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = xresources['*color4']

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = xresources['*background']

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = xresources['*color4']

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = xresources['*background']

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = xresources['*color4']

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = xresources['*background']

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = xresources['*color4']

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = xresources['*background']

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = xresources['*color4']

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = xresources['*background']

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = xresources['*color6']

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = xresources['*background']

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = xresources['*color5']

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = xresources['*background']

# Background color of the progress bar.
c.colors.statusbar.progress.bg = xresources['*background']

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = xresources['*color8']

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = xresources['*color6']

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = xresources['*color4']

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = xresources['*color4']

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = xresources['*color4']

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = xresources['*color6']

# Background color of the tab bar.
c.colors.tabs.bar.bg = xresources['*background']

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = xresources['*color4']

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = xresources['*color4']

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = xresources['*color6']

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = xresources['*color4']

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = xresources['*background']

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = xresources['*color4']

# Background color of unselected even tabs.
c.colors.tabs.even.bg = xresources['*background']

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = xresources['*background']

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = xresources['*color6']

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = xresources['*background']

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = xresources['*color6']

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = xresources['*color6']

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = xresources['*color0']

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = xresources['*color6']

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = xresources['*color0']

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = xresources['*color0']

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = xresources['*color4']

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = xresources['*color0']

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = xresources['*color4']


c.colors.webpage.bg = xresources['*background']
