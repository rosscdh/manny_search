Manny Search
------------

Elastic search demo for ManualOne


Installation
============

** Basic setup if you have not installed virtualenv (which is like rvm gemsets) **

1. easy_install pip (may need sudo)
2. pip install virtualenv virtualenvwrapper
3. export WORKON_HOME=~/.virtualenvs
4. mkdir -p $WORKON_HOME
5. source /usr/local/bin/virtualenvwrapper.sh
6. mkvirtualenv manny_search (workon manny_search if it doesnt automatically put you in the venv)

** App setup **

1. pip install -r requirements.txt
2. install elasticsearch and get it running on the default ip:port (http://127.0.0.1:9200/)
4. ./manage.py syncdb
5. manage.py loaddata product.json
6. ./manage.py runserver_plus
7. http://localhost:8000/api/v1/products/
8. http://localhost:8000/api/v1/products/?q=<:name_of_product_or_brand_any_ordeR_any_partial>

** admin **

1. http://localhost:8000/admin
2. login using the username/pass you entered when running *syncdb* (app setup:4)
3. add edit remove the products and brands

** load your data **

1. hook the database up to your mysql database
1. use manage.py inspectdb > our-schema.py  # this will provide you with the django models used to access the tables
3. copy the product and brand table to the product app
4. manage.py rebuild_index -v  # to repopulate elasticsearch with your data

** elastic search **

1. ./manage.py to see a list of commands available
2. ./manage.py rebuild_index to rebuild the elastic search data
3. ./manage.py update_index to update the elastic search data
4. when you modify items in the /admin system it will automatically update/add/delete etc the items from elasticsearch

** Extras **

1. Ask ross to talk about postgres HSTORE
2. if not postgres HSTORE then at least look at using a JSONField object which makes the schema more mallable
3. Ask ross about advanced indexing and filtering
4. Ask ross if none of this makes sense