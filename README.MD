# Mineral Catalog With Django

This project takes the previous mineral catalog project and adds a feature to search information and filter it to match user preferences.

Website that displays information about various minerals (AKA rocks). The home page of the site contains a list of all of the minerals in a database. Clicking on a mineral's name opens a page that displays information about the mineral.

Some other features are a search field to search for minerals, the ability to filter minerals by first letter name, filtering minerals by group and filtering minerals by color.

To run the server in Django, please run the following command in bash:

```bash
$ python3 manage.py runserver
```

This is a basic Django project. The script will construct a mineral model instance for each mineral in minerals.json and saves them to a SQLite database. The minerals, images and descriptions are displayed on an HTML webpage. Test functions and model creations are also included.

### Application Requirements

Run the following in bash:

```bash
$ pip3 install requirements.txt
```