# TODO

## Webview UI

* Python 3 compatibility for webview on Android: https://github.com/kollivier/pyeverywhere/blob/master/src/pew/kivy_pew/webview.py
* Back button goes back in history (instead of quitting): https://github.com/suchyDev/Kivy-Dynamic-Screens-Template/blob/master/screens/screenwebview.py

## Zim reading

* Converter Zim note -> HTML (with minimal dependencies to be maximally compatible with Android)
* Make the wsgi server a dynamic content generator
* Build notes tree
* Allow to setup config from wsgi server (Zim notes location, store multiple zim notes "books"/folder to quickly jump from one to the other, etc)

## Zim editing

WYSIWYG would be perfect but will be challenging. Basically, there are two ways:

* using a textarea that gets styled, but it can get out of sync very easily with the hidden underlying content.
* using contentEditable property of div and MutationObserver.

This last option seems the best. The idea would be to do both block-level and inline-level markup parsing, by sending the changes back to the webserver, which would add the content to the origin Zim note and convert to HTML to send back to the current window, in order to show a nicely formatted text.

BUT: need to find an ergonomic way to enable contentEditable=True, because it cannot be all the time enabled (else links are unclickable!) -> an "Edit mode" link, at the top of the screen and which would always be contentEditable=False, would be a good way! Or by double tapping a text area (and double tapping again would disable).

The best tutorial is probably this one:

[DIY tutorial using contentEditable property of div and MutationObserver](http://pothibo.com/2015/3/building-a-markdown-editor) ([mirror here](https://web.archive.org/web/20170616192810/http://pothibo.com/2015/3/building-a-markdown-editor))

Here are some projects implementing this approach for Markdown, can be good for inspiration:

* A Python based one to convert back and forth to Markdown (can be a good inspiration): http://md-wysiwyg.sourceforge.net/
* https://github.com/IonicaBizau/medium-editor-markdown
* https://github.com/sofish/pen#readme
* https://github.com/bergie/hallo
* http://marklighteditor.com/ (quite interesting as it allows on the fly rendering after typing markup, instead of highlighting and clicking on a button - this would be super useful on a mobile app)
* [Another list of WYSIWYG Markdown editors](https://softwarerecs.stackexchange.com/a/30531/16275).

## Packaging

Make a python-for-android or Buildozer packaging recipe.

