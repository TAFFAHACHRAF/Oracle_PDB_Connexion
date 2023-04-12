# FastAPI Oracle Connection Example

This project demonstrates how to connect to an Oracle database using FastAPI and cx_Oracle.

## Getting Started

To get started, make sure you have an Oracle database running on your machine. Replace the `host`, `port`, `sid`, `pdb`, `username`, and `password` values in the code with the appropriate values for your database.

Once you have updated the values, run the following command to install the dependencies:

```bash
pip install -r requirements.txt

Then, run the following command to start the FastAPI server:
uvicorn main:app --reload

You can then access the server at http://localhost:8000.

Usage
There is only one endpoint in this project, located at the root path ("/"). When you send a GET request to this endpoint, the server will return the message "Hello, world!".

Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.


N'oubliez pas de personnaliser le titre, la description, les instructions d'installation, d'utilisation et de contribution en fonction de votre projet.

