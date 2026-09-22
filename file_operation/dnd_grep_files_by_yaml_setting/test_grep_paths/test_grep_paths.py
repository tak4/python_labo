from pathlib import Path

from ..dnd_grep_files import KeywordSearcher


def test_GrepPaths():
    gp = KeywordSearcher(['D:/develop/github/python_labo/file_operation/dnd_grep_files/log'])
    gp.execute()


def test_GrepPaths_reports_progress():
    root = Path(__file__).resolve().parent.parent
    progress_updates = []

    gp = KeywordSearcher([str(root)])
    gp.execute(progress_callback=lambda message, current, total: progress_updates.append((message, current, total)))

    assert progress_updates
    assert any(current >= 0 for _, current, _ in progress_updates)