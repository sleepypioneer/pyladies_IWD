import unittest
from datetime import date

from IWD import PyladiesChapter as ChapterClass
from IWD import PyladiesIWD as IWDClass


class TestPyladiesChapter(unittest.TestCase):
    test_chapter = ChapterClass('test_chapter', 100)

    def test_get_name(self):
        expected = 'test_chapter PyLadies'
        name = self.test_chapter.get_name()

        self.assertEqual(expected, name)


class TestPyladiesIWD(unittest.TestCase):
    test_IWD = IWDClass()
    year =  date.today().year

    def test_add_chapter(self):
        for i in range(4):
            self.test_IWD.add_chapter(ChapterClass(f'test_chapter_{i}', 100))

        self.assertEqual(len(self.test_IWD.chapters), 4)

    def test_get_chapter_names(self):
        expected = [
            'test_chapter_0 PyLadies',
            'test_chapter_1 PyLadies',
            'test_chapter_2 PyLadies',
            'test_chapter_3 PyLadies'
        ]
        chapters = self.test_IWD.get_chapter_names()

        self.assertEqual(len(chapters), len(expected))
        self.assertEqual(chapters[0], expected[0])

    def test_get_total_members(self):
        expected = 400
        total_members = self.test_IWD.get_total_members()

        self.assertEqual(expected, total_members)

    def test_get_message(self):
        expected = f'Happy international Women\'s Day {self.year} \n\n' + \
            'Chapters world wide: \n' + \
            '* test_chapter_0 PyLadies\n' + \
            '* test_chapter_1 PyLadies\n' + \
            '* test_chapter_2 PyLadies\n' + \
            '* test_chapter_3 PyLadies\n' + \
            '\n400 PyLadies members world wide!!'
        message = self.test_IWD.get_message()
        
        self.assertEqual(expected, message)


if __name__ == '__main__':
    unittest.main()