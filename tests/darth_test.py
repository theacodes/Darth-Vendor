"""Tests for the vendor module."""
import os.path
import sys
import unittest
 
import darth
 
class DarthTestCase(unittest.TestCase):
  """Tests for the vendoring virtualenv and paths."""
 
  def setUp(self):
    self.orig_sys_path = sys.path
 
  def tearDown(self):
    sys.path = self.orig_sys_path
 
  def isFooBar(self):
    import foo
    return foo.is_foo
 
  def isBarBar(self):
    import bar
    return bar.is_bar
 
  def testAddVirtualenv(self):
    self.assertRaises(ImportError, self.isFooBar)
    darth.virtualenv(os.path.join(os.path.dirname(__file__), 'testdata', 'venv'))
    self.assertEquals(True, self.isFooBar())
 
  def testAddSite(self):
    self.assertRaises(ImportError, self.isFooBar)
    darth.vendor(os.path.join(os.path.dirname(__file__), 'testdata', 'site'))
    self.assertEquals(True, self.isBarBar())
 
if __name__ == '__main__':
  unittest.main()
