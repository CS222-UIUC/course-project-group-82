
import unittest   # The test framework
import sys
sys.path.insert(1, "G:\UIUC\cs\cs222\course-project-group-82\Source")
import Source.Speech_to_text as s
import filecmp
f1 = "Speech_Test\quick_speaker.txt"
f2 = "Speech_Test\slow_speaker.txt"
f3 = "output.txt"
class Test_TestIncrementDecrement(unittest.TestCase):
    def test_slow_speak(self):
        s.speech_to_text()
        result = filecmp(f1, f3, shallow = False)
        self.assertEqual(0, result)

    def test_quick_speak(self):
        s.speech_to_text()
        result = filecmp(f2, f3, shallow = False)
        self.assertEqual(0, result)

if __name__ == '__main__':
    unittest.main()