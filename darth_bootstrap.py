import os
import shutil
import darth


def bootstrap():
  cwd = os.getcwd()
  appengine_config_path = os.path.join(cwd, 'appengine_config.py')

  print('Copying darth.py to the current directory...')
  shutil.copyfile(darth.__file__.replace('pyc', 'py'), os.path.join(cwd, 'darth.py'))
  print('Copied!')

  if os.path.exists(appengine_config_path):
    print("""
You already have an appengine_config.py file in this directory so darth will not create one for you.

To make sure third party packages are available, please include the following lines in your appengine_config.py:

    import darth
    darth.vendor('lib')
""")

  else:
    print("Creating appengine_config.py")
    with open(appengine_config_path, "w") as f:
      f.write("""
# Use darth to setup the third-party packages folder
import darth
darth.vendor('lib')
""")

  print("""Darth bootstrapping complete.

You can now install packages using "pip install -t lib package-name" and import them as usual.""")
