# DEBUG GUIDE Template Version
DEBUG GUIDE Template Ver.   : Ver. 1.3 <br>
Last Modified Date          : 25 Nov 2022 <br>

## BUGS Catolog
1. name '__file__' is not defined <br>
2. BUG2 <br>
3. ... <br>
4. ... <br>




### BUG1:   name '__file__' is not defined
##### Error Messages
```python
NameError                                 Traceback (most recent call last)
Cell In [2], line 1
----> 1 absolute_path = os.path.dirname(os.path.abspath(__file__))
      2 relative_path = ""
      3 full_path = os.path.join(absolute_path, relative_path)

NameError: name '__file__' is not defined
```

##### Description
This error comes when you append this line os.path.join(os.path.dirname(__file__)) in *python interactive shell*.

*Python Shell* doesn't detect current file path in __file__ and it's related to your filepath in which you added this line

##### Solution
So you should write this line os.path.join(os.path.dirname(__file__)) in *file.py*. and then run python file.py, It works because it takes your filepath.


### BUG2
##### Error Messages

##### Description

##### Solution
