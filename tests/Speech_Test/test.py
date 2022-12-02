
from msilib.schema import Error
import unittest   # The test framework
import sys
sys.path.insert(0, 'G:/UIUC/cs/cs222/course-project-group-82/Source')
from Speech_to_text import speech_to_text as s
import filecmp
f1 = "Speech_Test/Continuous.txt"
f2 = "output.txt"
f3 = "Nothing.txt"
class Test_TestIncrementDecrement(unittest.TestCase):
    def test_speak_nothing3s(self):
        try:
            s.speech_to_text()
        except speech_recognition.WaitTimeoutError:
            result = filecmp(f3, f2, shallow = False)
            self.assertEqual(0, result)

    def test_Interminent_2s(self):
     with self.assertRaises(WaitTimeoutError, "listening timed out while waiting for phrase to start") :
            s.speech_to_text()

    def test_conitunous(self):
        try:
            s.speech_to_text()
        except:
            result = filecmp(f1, f2, shallow = False)
            self.assertEqual(0, result)
if __name__ == '__main__':
    unittest.main()
