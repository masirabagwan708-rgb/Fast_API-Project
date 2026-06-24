def NoteEntity(item) -> dict:
    return {
         "id" : str(item["_id"]),
         "title": item["title"],
         "desc": item["desc"],
         "important": item["important"],
    }
def notesEntity(items)-> list :
    return [notesEntity(items) for item in items]