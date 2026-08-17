Key findings:

1. src/ingestion/parse.py:45 : module-level chunk(...) call fires on import, so cli.py runs the full docling pipeline twice per execution. Wrap line 45 inside "if name == 'main':".
2. requirements.txt : empty file. you should run in terminal "pip freeze > requirements.txt" to document your python library dependencies
3. parse.py:39-42 : old comment, not relevant anymore
