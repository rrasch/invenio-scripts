## Multiple storage locations

###

The first thing we need to is create a suppressed location

```
pipenv run invenio files location suppressed /mnt/suppressed
```

The next thing we need to do is modify the files REST API
to pass in a location paramater when creating new files.  Here
are the proposed changes:

https://github.com/inveniosoftware/invenio-files-rest/compare/master...rrasch:invenio-files-rest:master

We then need to make sure we have the proper rest permissions:

```
invenio access allow files-rest-location-update role administration
invenio access allow files-rest-location-update role admin
invenio access allow files-rest-location-update:* role administration
invenio access allow 'files-rest-location-update:*' role administration
invenio access allow administration-access role admin
invenio access allow administration-access role adminUV@test.com
invenio access allow superuser-access role 'adminUV@test.com'
invenio access allow files-rest-location-update:* role administration
invenio access allow -a '*' files-rest-location-update role administration
```

The following is a python script that utilizes this new parameter:

https://github.com/rrasch/invenio-scripts/blob/main/create-bucket.py

In the script we create a dictionary with the key set to location
adn the value set to suppressed:

```
data = {"location": "suppressed"}

api_url = f"{args.invenio_url}/api/files"

response = requests.post(
    api_url, headers=headers, data=json.dumps(data), verify=False
)
```


