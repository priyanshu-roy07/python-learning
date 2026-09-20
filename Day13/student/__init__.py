"""
Historically, __init__.py was used to tell Python:

"Treat this directory as a Python package."

In modern Python, regular packages can also work without __init__.py because of namespace packages. But you'll still see __init__.py extremely often in real Python projects, and it can be used to initialize a package or expose selected names.

For now, it can simply be empty.
"""


"""
# One useful package structure

my_backend/
│
├── main.py
│
├── database/
│   ├── __init__.py
│   └── connection.py
│
├── models/
│   ├── __init__.py
│   └── user.py
│
├── services/
│   ├── __init__.py
│   └── user_service.py
│
└── utils/
    ├── __init__.py
    └── helpers.py
"""