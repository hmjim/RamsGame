[app]

# (str) Title of your application
title = Rams Online

# (str) Package name
package.name = rams_online

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ramsgame

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when installing dists.
android.accept_sdk_license = True

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = python3,kivy,python-socketio,websocket-client,requests,urllib3
requirements = python3,kivy,python-socketio,websocket-client,requests,urllib3

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (list) Android architectures to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables Android auto backup feature (Android API >= 23)
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
