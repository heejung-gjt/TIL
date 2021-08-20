"""
vs code에서 실행시키려고 하니 발생한 에러이다. 한글 주석을 남겨놓은 것이 문제가 된 상황으로 해당 문제는 한글 인코딩 문제이다. 파이썬 코드 최상단에 한글 인코딩을 명시해주면 해결된다 
SyntaxError: Non-ASCII character '\xea' in file Data Structure/recursive.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
pep8 site : https://www.python.org/dev/peps/pep-0263/
"""
# -*- coding: utf-8 -*-

