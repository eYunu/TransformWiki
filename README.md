# TransformWiki



* Deployment instructions
### Production

Uses gunicorn + nginx.

1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build 
    or
    $ docker-compose -f docker-compose.prod.yml up --build
    ```
    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
