# Riddle Game

## Description
This is a simple web application that presents users with a riddle and allows them to submit answers.

This project was carried out as part of the "5I-SY3 Virtualisation" course supervised by Mr. Benoit Charroux.

The project was made by Melvyn Dao and Matthieu Phommachanh.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- Docker
- Kubernetes

## Setup Instructions
1. Clone this repository to your local machine.
2. Make sure you have Docker installed on your system and a Docker Hub account.
3. Login onto Docker Hub using `docker login`.
4. Navigate to the project directory in your terminal.
5. Build the Docker image using the command `docker build -t <your-docker-hub-username>/game-service:v1 .`.
6. Push the Docker image onto Docker Hub `docker push <your-docker-hub-username>/game-service:v1`.
7. Replace the image in the `game_service-deployment.yaml` file with the one you pushed on Docker Hub.
8. Start minikube using the command `minikube start`.
9. Enable the NGINX Ingress controller using the command `minikube addons enable ingress`.
10. Apply the 3 different YAML files using `kubectl apply -f <yaml-config-file-name.yaml>`.
11. Retrieve the IP address of your ingress using the command `kubectl get ingress`.
12. On Linux, edit the `/etc/hosts` file with your preferred text editor and add both the `ADDRESS` and `HOSTS` values of your Ingress at the bottom of the file.

## Usage
- Upon accessing the application, users will see a riddle displayed on the screen.
- Users can enter their answer in the input field provided and click the "C'est parti !" button to submit their answers.
- The application will tell the user whether the submitted answer is correct or incorrect.

## Future Improvements
- Add more riddles to increase variety.
- Add a second service to manage the riddles by making use of a MySQL database to store both riddles and their answers.
- Implement a random riddle generator to provide a new riddle for each session.
- Improve the styling and user interface of the application.
