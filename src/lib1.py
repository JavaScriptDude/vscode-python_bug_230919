'''
    # Test setup instructions:
    # Create Symbolic link for lib2.py
    % cd <workspace_root>
    % ln -s `pwd`/other/lib2/src/lib2.py `pwd`/lib/lib2.py
'''

import lib2
import lib3

def main():
    lib2.lib2_foo()
    lib3.lib3_foo()

if __name__ == '__main__':
    main()