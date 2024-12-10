# Installation

**1. clone the repository and cd into the folder**
 ```
 git clone https://github.com/khisareuben/Django-CRM-project.git && cd Django-CRM-project/
 ```
**2. Create a virtual environment and activate it**
```
py -m venv env

source env/Scripts/activate  #for windows
source env/bin/activate      #for mac/linux
```

**3. Install the requirements**
 ```
 pip install -r requirements.txt
 ```

**4. Inside `settings.py` and `mysqldb.py` Change username and password to your mysql credentials**


**5. run the `mysqldb.py` to create the database**
```
python  mysqldb.py
```

**6. Make the migrations and migrate**
```
python manage.py makemigrations
python manage.py migrate
```

**7. Finally run the server**
```
python manage.py runserver

```
