# Extract Objects from Images with transparent background

This project is a Python application that extracts and saves objects from 
images. It uses OpenCV and Pillow libraries to process images and extract 
objects based on contours.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installing

#### From Docker Hub

```bash
docker pull vovan/extract_subimages
```

[DockerHub page](https://hub.docker.com/r/vovan/extract_subimages)

#### From GitHub

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to build and start the Docker container:

```bash
docker-compose up --build
```

This will start the Python application inside a Docker container. The 
application will process images from the `input` directory and save the 
extracted objects to the `output` directory.

## Usage

Place your images in the `input` directory. The application will process these 
images and save the extracted objects to the `output` directory.

## Built With

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

## Authors

- vovanmozg

## License

This project is licensed under the MIT License.
