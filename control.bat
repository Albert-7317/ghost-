@ECHO OFF

COLOR 2
GOTO python

::Running the pythonscript
:python
START safe.py
GOTO end



::standard finish
:end
COLOR 7
TIMEOUT 3
