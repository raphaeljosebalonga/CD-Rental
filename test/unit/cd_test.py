import sys
sys.path.insert(0, '../../')

import unittest

from cd.cd import Cd

class TestCD(unittest.TestCase):
	def test_cd_object_can_be_created(self):
		cd = Cd(1, "Insert Disc", False)
		self.assertEqual(cd.cd_id, 1)
		self.assertEqual(cd.rented, False)

if __name__ == '__main__':
	unittest.main()