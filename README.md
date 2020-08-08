# User-activity-period
Back-end for user-activity data
> Deployed on - https://activity-period.herokuapp.com/

> Works with Python 3

## Usage -
* Install requirements - `pip3 install -r requirements.txt`
* Run migrations - `python3 manage.py migrate`
* Run server - `python3 manage.py runserver`

## API Endpoint -
* `/api/get_members` - Get the list of all members and their respective activity periods.

## Management Command - 
`loaddata` is a custom management command created to load batch data into the database from a json file.


**usage** -`python3 manage.py loaddata <json-file-name>`
