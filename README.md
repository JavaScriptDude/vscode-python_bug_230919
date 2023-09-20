# vscode-python_bug_230919
Bug related to symlinks in PYTHONPATH

Visual Studio Code should be able to reconsile all python libraries found in PYTHONPATH whether they are a symbolic link or otherwise.

VSCode has recently made changes that breaks support for symbolic links and this repo illustrates this issue.

This repo is a contrived example of a common project setup usecase I deal with.

To set up:
* downlaod this repo
* Open in visual studio code on Linux
* Open VSCode Terminal and set up symlink to a library:
```
    # Note: you should be in the workspace root 
    % ln -s `pwd`/other/lib2/src/lib2.py `pwd`/lib/lib2.py
```

Open `src/lib1.py` in vscode

It should load without any warnings however it presently shows:
```
lib1.py
  Import "lib2" could not be resolved" [Ln 8, Col 8]
```

