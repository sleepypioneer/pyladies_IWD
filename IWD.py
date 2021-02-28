from datetime import date


class PyladiesChapter:

    def __init__(self, location: str, number_of_members: int, website: str = None):
        self.location = location
        # self.existing_since = existing_since existing_since: date.year,
        self.number_of_members = number_of_members # if number_of_members is not None else 0
        self.website = website if website is not None else 'https://pyladies.com/'

    def get_name(self):
        return f'{self.location} PyLadies'


class PyladiesIWD:

    def __init__(self):
        self.chapters = []
        self.year = date.today().year

    def add_chapter(self, chapter: PyladiesChapter):
        self.chapters.append(chapter)

    def get_message(self):
        message = f'Happy international Women\'s Day {self.year} \n\nChapters world wide: \n'

        chapter_names = self.get_chapter_names()

        for name in chapter_names:
            message = message + '* ' + name + '\n'

        total_members = self.get_total_members()

        message = message + f'\n{total_members} PyLadies members world wide!!'
        
        return message

    def get_chapter_names(self):
        chapter_names = []
        for chapter in self.chapters:
            name = chapter.get_name()
            chapter_names.append(name)
        
        return chapter_names

    def get_total_members(self):
        total_members = 0
        for chapter in self.chapters:
            total_members += chapter.number_of_members
        return total_members


if __name__ == '__main__':

    berlin_chapter = PyladiesChapter('Berlin', 2010, 'http://berlin.pyladies.com/') #date.year(2014)
    hamburg_chapter = PyladiesChapter('Hamburg', 646, 'http://hamburg.pyladies.com/') #date.year(2019),

    IWD_2021 = PyladiesIWD()

    IWD_2021.add_chapter(berlin_chapter)
    IWD_2021.add_chapter(hamburg_chapter)

    IWD_message = IWD_2021.get_message()

    print(IWD_message)