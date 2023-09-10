# R214220704
SUBMITTED BY - MITALI CHAUDHARY
SAP ID - 500084412
B.tech CSE CSF


CAMPUS HIRING EVALUATION - FRONTEND FOR "AFFORDMED TECHNOLOGY, INNOVATION & AFFORDABILITY"

QUESTION - Develop Number Management HTTP Microservice 
# Number Management Service

The Number Management Service is a simple HTTP microservice built with Flask that retrieves and merges unique numbers from multiple URLs, and then returns them in ascending order. It's designed to be lightweight and efficient.

## Table of Contents

- [Usage](#usage)
- [Endpoints](#endpoints)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Service](#running-the-service)
- [Example](#example)

## Usage

This service allows you to fetch and merge numbers from different remote URLs and retrieve them in ascending order. It's useful for collecting and managing numeric data from various sources.

## Endpoints

- `/numbers`: This endpoint retrieves numbers from specified URLs and returns them in ascending order.

## Dependencies

This service uses the following Python libraries:

- Flask: A micro web framework for building web applications.
- Requests: A library for making HTTP requests to remote URLs.

## Installation

1. Clone the repository:

   ```shell
   git clone <repository-url>
   cd number-management-service
Install the required dependencies:

shell
Copy code
pip install Flask requests
Running the Service
You can start the service by running the following command:

python app.py
The service will be accessible at http://localhost:8008.
Example
Suppose you have the service running locally, and you want to retrieve numbers from remote URLs. You can make a GET request to the /numbers endpoint with the url query parameter.
Example:

shell
Copy code
curl "http://localhost:8008/numbers?url=http://20.244.56.144/numbers/primes&url=http://20.244.56.144/numbers/fibo&url=http://20.244.56.144/numbers/odd"
This will return a JSON response with merged unique numbers in ascending order.

json
Copy code
{
  "numbers": [1, 2, 3, 5, 7, 8, 9, 11, 13, 15, 17, 19, 21, 23]
}
