# EAU2
Thus far we have developed up until Milestone 3. Our project includes a dataframe, an adapter, a key and a kv store. It also includes a node for future development of the multiple node system. 

## Getting Started
Our software is contained within our src folder. 
It includes:
    adapter.py: The software that contains the adapter that reads in a singlular file as part of its constructor. 
                In order to create an adapter class you must create the object: Adapter(file_name)
                In order to create a data array (a 2D array of data) you must call the function create_dataframe function: adapter.create_dataframe(start_index, end_index)
                The adapter also determines the schema of the file it was given, in order to retrieve the schema, one must call the function retrieve.schema on their adaper object

    application.py: The application object is currently a place holder for the future implementation of the application layer that we be implemented
                    It currently only contain two fundamental functions, run (that currently does not do anything) and this_node that returns the node idx.
                
    client.py: This piece of software is part of our overall node class. It is a multithreaded client that deques and enques to a common queue
               The importance of this file is to ensure we have a tested version of a larger node that we will be implementing in the future milestones

    dataframe.py: Is an object that represents a data structure recieved from the adapter. 
                  The dataframe takes in a 2D array of data (extracted fromt the adapter), a schema (also extracted from the adapater), a key given at the application layer and a kv store that lives on the node. With all this information, the dataframe constructs and object that ties a value to a key and places it into the kvstore. This reduces code duplication and ensures that the dataframe only lives in one place at a given time.
                  One is also able to create a dataframe from an array (single) and from a scalar value. These function from_array and from_scalar respecitively are constructors in their own rights.
    
    demo.py: Contains the demo code given in milestone 1. It was fully implemented and tested for funtionality.

    kv_store.py: This file contains two objects, a Key object and a KV store object.
                 The key object, has a unique string associated with it along with a integer value that represents the home node of the key
                 The KV store is a dictonary of keys and their associated values (the dataframe). The keys are placed into the kv store after ensuring that a) their home node aligns with the home node of the kv store and b) the key name is unique.
                 The KV store currently simply handles adding to its ranks and removing from its store. It recognises when a key is foreign and prints a message to the console. This is only for the time being so we may succesfully implement a network layer.
    
    main.py and mainUI.py: These two files work hand in hand with one another. As the name suggests mainUI, contains the UI created in milestone one.
                           The UI, though not fully used in Milestone 3 is continuing to be developed to handle sending commands with an easy to use GUI feature. (An addition to our efforts, but one we thought would be useful as developer providing software to a client, we would want it to be as smooth and inituative as possible.)
    
    node.py: Contains a very fundamental code of a node system. This system is not threaded. This is the core fundamental we are working with in 
             relation to client.py and server.py to make sure our system is running as expected when we begin to develop the network layer.

    schema.py: Is an object that represents a schema. A schema contains a list of types along with the number of rows and columns of that 
               particular dataframe

    server.py: Was developed with client.py. It's intended for using it as a multi threaded network. With one system sending commands at a continous 
               stream, and the second thread recieving commands and executing them. 

    simple_thread.py: Was developed to test threading and queueing for the execution of server.py and client.py. 
                      It is used to ensure threading logic is safe.

    sor_create.py: Is the script we use to generate data into an sor file

    threaded_kvstore.py: The threaded kv store was created to imitate the network layer and complete milestone 3.
                         It creates two kv stores, one with two keys and one with none. The second kv store sends a command to the first to retrieve the dataframe contained within the key it asks for, the second command recieves the command and prints the data to the console for validity. 

    utils.py: Is a common library shared across the entire code base to reduce repetative code. It has some functions multiple parts of the system requires.
    

## Building the Code

Since our project is written in python, to run the code refer to the Makefile. When the project is started, the Makefile should be in the same directory as the milestone_3 folder. This way you only have to 'make run' and make test' to see the output.

All the files in our project should have relative paths to the milestone_3 project. In Python each folder that has a file called '\_\_init\_\_.py' is considered a module. This means that files can import from other files in that module. Our entire project imports assuming that milestone_3 is a module, as well as the subfolders src and tests.



## Running the tests




## Authors

* **Lucas Calero Forero**
* **Eden Desta**