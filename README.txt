============
  FOX Py
============

FOX Py provides an interface to FOX Federated Knowledge Extraction Framework.
it most useful for tasks involving entity recognition inside the text corpora.
Typical usage often looks like this:
```
#!/usr/bin/env python

from foxpy import FOX
fox = FOX()
text = "London Idaho Hawaii"
response = fox.recognizeText(text)
```
For more information refer to test cases in [tests/foxpy](tests/foxpy) folder.

Contributors
=========

* Ivan Ermilov (AKSW/BIS University of Leipzig)

Notes
=========

The source code is available from:
https://github.com/earthquakesan/fox-py
