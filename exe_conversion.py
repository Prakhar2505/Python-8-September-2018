'''
my_cx_freeze.py
To run code from cmd
python my_cx_freeze.py build
Eksp from cmd:
C:\Python32\Scripts>python my_cx_freeze.py build
'''
import os
import sys
from cx_Freeze import setup, Executable
includes = []
includefiles = ['E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\GUI_With_Disable.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\FRI_TL.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\classify.py',
                "E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\\vgg16.py",
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\._FRI_TL.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\._classify.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\._vgg16.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\._images']
# excludes = []
packages = ['os', 'matplotlib', 'keras', 'sklearn', 'imutils', 'numpy', 'random', 'cv2', 'time']

PYTHON_INSTALL_DIR = sys.executable
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = 'Win32GUI' if sys.platform == 'win32' else None

exe = Executable(
    script = r"E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\GUI_With_Disable.py",
    base = base
)

options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            # includefiles
         ],
        # 'packages': packages,
    },
}

# filename = "GUI_With_Disable.py"
setup(
    name = 'Setup',
    version = '1.0',
    description = 'DL Project',
    # options = options,
    author = 'Ankit Verma',
    # author_email = 'someting@my.org',
    options = {
        'build_exe': {
            'include_files':[
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\GUI_With_Disable.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\FRI_TL.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\classify.py',
                "E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\\vgg16.py",
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\._FRI_TL.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\._classify.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\._vgg16.py',
                'E:\Gurjas\Course Syllabus\Machine Learning\Python-ML-Course\Projects\._images'
             ],
            'packages': packages,
        },
    },
    # options = {'build_exe': {'packages':packages,'includes':includes, 'include_files': includefiles}},
    # executables = [Executable(filename, base = "Win64GUI", icon = None)]
    executables = [exe]
)
