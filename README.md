rest_api for Lineage
=============
This library contains all core functionality for the lineage Rest API used as an entry point to get and push entities to atlas.
This API creates entities one at a time but can be a service connected to an infrastructure as code.
Each entrypoint (one for each type definition) contains two calls a get and a post.
The get call returns the number of entities of the type and a list of their qualifiedNames.
The post call takes in parameters defined in the swagger, and creates the entity of the type with the parameters defined in atlas. The response will tell how many entities were created, updated and deleted. 
For a full list of the types supported, and the required fields to define the type, please look at the swagger documentation.


## Installation
Make sure to have Python3 with Virtualenv and Git installed 

Open Terminal to current directory (this folder, clone if needed)
create venv and install requirements (windows)
```
$   virtualenv -p python3 venv

$   source venv/Scripts/activate

(venv) $ pip install -r requirements.txt

(venv) $ python setup.py develop


```

## Configurations and Credentials
Please make a copy of `config.sample.py` and `credentials.sample.py` and rename the files to `config.py` and `credentials.py` respectively.
Please set the configuration parameters and credentials for `atlas`.

| Name | Required | Description | 
|---|---|---|
| atlas.server.url | True |  The Server Url that Atlas runs on, with '/api/atlas' post fix. | 
| atlas.credentials.username | True | The Username to be used to access the Atlas Instance. | 
| atlas.credentials.password | True |The Password to be used to access the Atlas Instance must correspond to the Username given. | 

## API Setting
In ``rest_api/settings.py`` set the desired url and port to run the api service in the setting ``FLASK_SERVER_NAME``.

## Execution
1. Create the Python Environment. How to do this can be found in this file under `Installation` 
2. Fill in the Configurations and Credentials as indicated in this file under `Configurations and Credentials` 
3. Run ``python -m rest_api.app`` in the terminal to start the API.

In the browser, open the URL http://``FLASK_SERVER_NAME``/lin_api/

To look at Swagger open URL http://``FLASK_SERVER_NAME``/lin_api/swagger.json



#############################################################################################################

### More detail on the API can be found on <a href="m4i_README.md">m4i_README</a>

## Testing

This project uses `pytest` as its unit testing framework.
To run the unit tests, please install `pytest` and create the atlas test environment, and then execute the `pytest` command from the project root folder.

Unit tests are grouped per endpoint.
Unit test modules are located in the same folder as their respective covered controller folder.
They can be recognized by the `test_`  name prefix, followed by the name of the covered module.

### How to make atlas test Environment
1. Start the docker container with atlas on it
```
docker pull wombach/docker-apache-atlas:latest

docker run -d -p 21000:21000 --name atlas wombach/docker-apache-atlas:2.2.0.1 /opt/apache-atlas-2.2.0/bin/startup.sh


user: admin
password: admin
```

2. Load the saved zipped test entities (response.zip) 
```shell
curl -g -X POST -u username:password -H "Content-Type:multipart/form-data" -H "Cache-Control: no-cache" -F data=@response.zip http://service:port/api/atlas/admin/import
```
### What we test for?
 - Tests are run through a test client of the app.
- We test the serializers, to make sure that what is needed is there else error.
- We test that the controllers work, and we check their potency or behaviour. 
  1. pushing the same request twice should not result in any audits
  2. pushing a change to an entity should result in an audit.  
- Any test that creates an entity, then also have to delete the entity when done.
  As when running the tests the new test expects that the entity does not exist previously. 
  Pytest allows for a file `conftest.py` where functions can be defined and available for all pytests. 
  The functions to check if the entity is made and to delete it.









