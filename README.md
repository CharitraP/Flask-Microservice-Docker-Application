1. A Flask microsevices application:
   * Takes in the json input and generates the unique hash key generated based on the fields,to make sure there is no two id's created for the same object passed.
   * The hash key is then used to store the object in the dictionary(for in-memory storage).
   * The application also has a function to caluculate the point secured by the receipt and that is retrived based on the hash key.
2. Application is pushed to Docker and the port number is explicitly provided on the run file. (port number:4000)
3. The application is tested using Postman to ensure it is working as expected.
4. The docker image is published onto github using github actions.
5. To downlad the image of the application execute the docker pull command.
6. To run the Container using docker run command.
7. To check the logs of the container use docker logs command.

#8. To see the Difference
