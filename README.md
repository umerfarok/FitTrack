# FitTrack

FitTrack is a Django application for tracking fitness activities.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher
- Pipenv

### Installation

1. Clone the repository:
```bash
git clone https://github.com/umerfarok/fittrack.git
```

2. Navigate to the project directory:
```bash
cd fittrack
```

3. Install the project dependencies:
```bash
pipenv install
```

4. Activate the Pipenv shell:
```bash
pipenv shell
```

1. Apply the migrations:
 ```bash
 python manage.py migrate
 ```

1. Create a superuser. This will prompt you to enter a username, email, and password:
```bash
python manage.py createsuperuser
```

### Running the Application

1. Start the Django server:
```bash
python manage.py runserver
```

2. Open your web browser and navigate to `http://localhost:8000`.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details