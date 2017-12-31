# Developer readme

This mockup app runs using Kivy, wsgiref and pywebview (desktop only) on Python >= 2.7.13. This document describes how to test it.

## Architecture

To ensure compatibility with Android, the application was split in two parts:

1. The UI's main.py (main_desktop.py for desktop computers)
2. The background webserver as a service, in service/main.py

When one launch main.py, the call to `AndroidService('ZimAndroidWebserver', 'running').start()` will launch whatever is in `service/main.py`.

`android.txt` is a simple file describing how to present the app in the Kivy Launcher (necessary else it won't display). It is useless for APK packaging.

## Running on desktop

To run on desktop, simply install pywebview module and then run `main_desktop.py`. Should work on Windows, Linux and MacOSX.

## Running on Android

The easiest way is to launch via the Kivy Launcher app.

A good development environment consists of:

1. Bluestacks emulator
2. TotalCommander app to copy from the Bluestacks shared folder in `sdcard/windows/BstSharedFolder` to `sdcard/kivy`.
3. Kivy Launcher, to launch the app without needing compilation (just need to copy the project folder into `sdcard/kivy`).
4. Launch `C:\Program Files (x86)\BlueStacks\HD-Adb.exe logcat > C:\temp\logcat.txt` to enable logcat debug log (necessary to track down errors and bugs).

Once you have all of these, it becomes very easy and fast to test any change you do, just copy/paste the new version of the scripts over the old ones in `sdcard/kivy`.

Note that Kivy Launcher has some limitations:

* Partial implementation of native Python libraries (eg, no wsgiref) and variables (eg, no IPv6 variables). However, the launcher supports any pure Python library, so wsgiref can be supported by copying the folder from python libs.

A limitation of Kivy for GUI is that for the moment it is not possible to add any other widget when using a webview (except for the magicians at [kivy-gmaps](https://github.com/tito/kivy-gmaps)).

However, using Kivy, it is possible to do pretty much anything that can be done via Java: use plyer to access Android libraries in a pythonic way (but with limited functionality), or pyjnius to have full access (but with less pythonic syntax).

Compiling an APK

To compile an APK, one need to use python-for-android (P4A), by the same authors as Kivy.

P4A can compile pretty much anything, but it needs a backend. For the moment, there are a few ones: SDL2 (default for Kivy apps) and flask. But potentially anything can be a backend, just a recipe is needed.

If the application is made with Kivy, we can use Buildozer, which is another layer on P4A to make building easier by using a buildozer.spec file instead of commandline arguments to P4A.

P4A can only run on Linux at the moment, so a good solution is to use the Kivy Virtual Machine. [Read this post for more info on the steps necessary](https://github.com/jaap-karssenberg/zim-android-mockapp/issues/4#issuecomment-354473348).

## Authors

Stephen Larroque & Jaap Karssenberg