from ..dnd_grep_files import GrepPaths

def test_GrepPaths():
    gp = GrepPaths(['D:/develop/github/python_labo/file_operation/dnd_grep_files/log'])
    gp.grep_target()