Darth-Vendor
============

Third-party vendoring helper for Google App Engine and other sandboxed python environments.


Hey, you! LISTEN!
-----------------

Darth is now part of the official Google App Engine SDK. **You don't need this library!**

To use with GAE, just create a ``appengine_config.py`` file like this:

```python
from google.appengine.ext import vendor

vendor.add('lib')
```

And pip with ``-t lib`` to install packages:

```
$ pip install -t lib gcloud
```

You can read more about vendoring in the [official docs](https://cloud.google.com/appengine/docs/python/tools/libraries27#vendoring).


Installation
------------

The easiest way to use darth is to install it globally on your system (this may require sudo):

    $ pip install darth

And then run the ``darth-bootstrap`` script in your project:

    $ cd my-appengine-project
    $ darth-bootstrap

This script will copy ``darth.py`` to your project and create an ``appengine_config.py`` if needed.

Alternatively, you can install darth directly into your project and create ``appengine_config.py`` manually.

    $ cd my-appengine-project
    $ pip install -t . darth


Usage
-----

If you used the ``darth-bootstrap`` script it will automatically create the appropriate ``appengine-config.py`` for you. If you already have an ``appengine-config.py`` or if you installed with the alternative method, you'll need to add these lines to your ``appengine_config.py`` to enable third-party packages:

~~~python
import darth
darth.vendor('lib')
~~~

You can replace ``lib`` with the folder you have chosen to store third-party packages in.


Installing packages
-------------------

Install packages using ``pip`` with the ``--target`` or ``-t`` option.

    pip install --target lib protopigeon
