# travel-pics
 Travel Pics is an invitation to explore the world through lenses. Here we can share special moments, stunning landscapes and travel tips. Feel free to contribute your comments, photos and suggestions!


## START
### On linux
```
python -m venv env
source env/bin/activate
```
### On windows
```
python.exe -m venv env
env\Scripts\activate
```
### Upgrade pip
```
python -m pip install --upgrade pip
```
### Install dependencies
```
pip install -r requirements.txt
```
### Or if you want to install the latest versions of google libraries
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### Create .env file
```
SECRET_KEY=your_secret_key
```
### Create apps
```
python manage.py startapp core
python manage.py startapp pics
```

