# Atlas M4I
There are 3 main parts to the REST API

1. The **app** that runs the rest API
2. The **API definition**    
3. The **controller** that defines REST request and functionality of the Entity/Process
   - The Model or **Serializer**

**Assumptions:**
- typeDefs are already Defined

- Referenced Entities already exist in Atlas

## App
The App contains the logic for configuring and 
starting the Flask app. Paths and blueprints 
are added here, linking to the different endpoints and namespaces.
The app is configured to a local host.

```
TO RUN THE APP IN TERMINAL type: python -m rest_api.app
```

## API Definition
With the use of 'flask-restplus' an api is defined. The controller endpoints and serializer models are all defined using flask restplus.
This package takes all this information to automatically generate interactive documentation for your API using Swagger UI.
With the use of flask-restplus, additions like new endpoints to the swagger documentation is simple

## Controller
The Controller sets the namespace, request methods, the expected
input and functionality todo with the request.
#### NameSpace:
The REST API itself is split into a number of separate namespaces. 
Each namespace has its own URL prefix and is stored in a separate 
file in the endpoints(process or entity) directory 
(example: lin_api/process/generic_process).
#### Request Method:
Determines the type of REST request that will be made. How to set request methods is as follows:
```
@app.route(some_route, methods=['GET' or 'POST' or 'PUT' or 'DELETE'])
```
#### Expected Input
The input is serialized using a 'model' defined with restplus.
How to set the expected input or request is as follows:
```
@api.expect(some_serializer_Model, validate=True)
```

#### Expected Output
The output is marshalled using a 'model' defined with restplus.
How to set the expected output is as follows:
```
@api.marshal_with(some_output_model)
```
For 'get' calls the output is expected to return the number of entities of the type and a list of their qualifiedNames.

For 'post' calls the output is expected a sum of how many entities were created, modified and deleted.

***Serializers***

A model is defined in the serializer file. It should
reflect the desired schema , while also stating what the is required, 
optional and other limitations. This is done flask-restplus fields, which can also be nested.





