
import unittest   # The test framework
import Source.Speech_to_text as s
import filecmp
f1 = "G:\UIUC\cs\cs222\course-project-group-82\.github\Speech_Test\quick_speaker.txt"
f2 = "G:\UIUC\cs\cs222\course-project-group-82\.github\Speech_Test\slow_speaker.txt"
f3 = "G:\UIUC\cs\cs222\course-project-group-82\output.txt"
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