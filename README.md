# A simple template of flask with factory pattern, Bootstrap

Include the following technologies:
1. Jinja2
2. python3 virtual environment
3. OS: Linux, fedora-34 KDE

### File structure

```bash
[chris@fedora style-bootstrap]$ tree -I 'env|__pycache__'
.
├── app
│   ├── __init__.py
│   ├── static
│   │   ├── scripts
│   │   │   └── login.js
│   │   └── styles
│   │       └── default.css
│   └── templates
│       ├── base.html
│       └── index.html
├── instance
│   └── development.yaml
├── README.md
├── requirements.txt
└── tags-search-information.txt

6 directories, 9 files
[chris@fedora style-bootstrap]$ 
```

### Important
> pip install -r requirements.txt

### Resources
* Markdown, web:commonmark [link](https://commonmark.org/help/)

### Flask run
    export FLASK_APP=appname
    export FLASK_ENV=development
    flask run --host=127.0.0.1 --port=5001