#empty lists to store data
users=[]
diaryEntries=[]


class DiaryEntry:
    def __init__(self, diaryTitle, date, diaryEntryBody, entry_id):
        self.diaryTitle = diaryTitle
        self.diaryEntryBody = diaryEntryBody
        self.date = date

    def __repr__(self):
        return repr(self.__dict__)
