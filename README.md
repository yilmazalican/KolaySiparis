![alt tag](http://imagizer.imageshack.us/v2/280x200q90/633/KSHvtG.png) 
# Welcome HACKER!

KolaySiparis is a open-source, strong level, scalable, fast, responsive online [food ordering] web application which is built by Django, a free and open source web application framework, written in Python v2.0, which follows the model–view–controller (MVC) architectural pattern.It is maintained by the Django Software Foundation (DSF), an independent organization.

#### TEAM MEMBERS
- @osmancicek
- @ozgemeva
- @yilmazalican
- @alimert

### KolaySiparis uses;
  - Python v2.7.10 
  - MySQL v5.6.27
  - pip v7.1.2
  - Virtual environment v13.11.12
  - Django v1.9
  - wheel v0.24.0
  - Bootstrap v3.3.4
  



### Version
1.0.1

### Installation
- You need to create a database for the project on your localhost, edit as yours;
/KolaySiparis/settings.py
```sh
DATABASES = {
    'default': {
    #it connects localhost serves by default
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'yourdbname',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
    }
}
```


- You need To Install git,
for more info: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

- You need a  to install a stable version python 2 native programming language.
```sh
$ brew install python
```
- Cloning the Repo into local machine
```sh
$ git clone git@github.com:yilmazalican/KolaySiparis.git
$ cd KolaySiparis
```

- Install virtual environment
```sh
$ pip install virtualenv
```
- Activate the virtualenv
```sh
$ source bin/activate
```
- Install the requirement django packages
```sh
 $ pip install -r requirements.txt
```
- Sync the database 
```sh
 $ python manage.py syncdb
```
- Migrate the db

```sh
 $ python manage.py makemigrations
```
- Run the local server 

```sh
 $ python manage.py runserver
```


### Development

Want to contribute? Great!

KolaySparis uses Git for fast developing.
 So What are you waiting for ? GO, Fork the Repo!



License
----

KolaySiparis uses MIT Licence. We are open source and stand forever.
