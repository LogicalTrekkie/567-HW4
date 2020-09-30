import unittest

from hw4 import git


class TestGit(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
	
	def testGit1(self): 
		self.assertEqual(git('logicaltrekkie'),['Repo cs146-example Number of commits 8' ,'Repo Repo1 Number of commits 1','Repo SSW Number of commits 8','Repo TriangleTestingHW2 Number of commits 17'],'Should show repos and amount of comits')

	def testGit2(self): 
		self.assertEqual(git("56757hdskjhdaca6"),'User DNE','Should Fail')
		
	def testGit3(self): 
		self.assertEqual(git(5),"Id not a String",'Should report not a string')
	

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)