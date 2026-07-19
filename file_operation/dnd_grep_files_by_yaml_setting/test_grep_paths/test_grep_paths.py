from ..dnd_grep_files import FileKeywordSearcher

def test_GrepPaths():
    gp = FileKeywordSearcher(['D:/develop/github/python_labo/file_operation/dnd_grep_files/log'])
    gp.search()