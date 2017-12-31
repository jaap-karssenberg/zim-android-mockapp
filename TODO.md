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

* WYSIWYG would be perfect but will be challenging. Can try one of the following:
  * [DIY tutorial using contentEditable property of div and MutationObserver](http://pothibo.com/2015/3/building-a-markdown-editor) ([mirror here][21])
  * A Python based one to convert back and forth to Markdown (can be a good inspiration): http://md-wysiwyg.sourceforge.net/
  * https://github.com/IonicaBizau/medium-editor-markdown
  * https://github.com/sofish/pen#readme
  * https://github.com/bergie/hallo
  * http://marklighteditor.com/ (quite interesting as it allows on the fly rendering after typing markup, instead of highlighting and clicking on a button - this would be super useful on a mobile app)
  * [Another list of WYSIWYG Markdown editors](https://softwarerecs.stackexchange.com/a/30531/16275).

## Packaging

Make a python-for-android or Buildozer packaging recipe.

