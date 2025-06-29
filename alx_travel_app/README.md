# ALX Travel App 0x01

## Milestone 3: Creating Views and API Endpoints

### Objective

This is a Django-based travel application API for managing listings and bookings, built as part of Milestone 3. We are to build API views to manage listings and bookings, and ensure the endpoints are documented with Swagger.

---

### Repository

- GitHub: [alx_travel_app_0x01](https://github.com/BunnyeNyash/alx_travel_app_0x01.git)
- Main Directory: `alx_travel_app`

### Project Structure
```
alx_travel_app_0x00/
├── alx_travel_app/
│   ├── listings/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed.py
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── alx_travel_app/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
├── README.md
```

### Key Files and Their Roles
- listings/models.py: Defines the database models:

  - Listing: Represents a travel listing.
  - Booking: Represents a user's booking for a listing.
  - Review: Represents a user's review of a listing.

- listings/serializers.py: Contains serializers for the Listing and Booking models, facilitating the conversion between model instances and JSON representations for API interactions.

- listings/management/commands/seed.py: Implements a custom Django management command to seed the database with sample data for testing and development purposes.

- listings/views.py: Contains view functions or classes to handle HTTP requests and return responses.

- listings/urls.py: Maps URLs to the corresponding views in the listings app.

- alx_travel_app/settings.py: Configures the Django project's settings, including installed apps, middleware, database configurations, and more.

- manage.py: A command-line utility that lets you interact with this Django project in various ways.

- requirements.txt: Lists the Python packages required to run the project.

- README.md: Provides an overview of the project, setup instructions, and other relevant information.


### How to Use
1. Clone the Repository

```bash
git clone https://github.com/BunnyeNyash/alx_travel_app_0x01.git
cd alx_travel_app_0x01
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run Migrations

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```


### API Endpoints
**Listings:**
- `GET /api/listings/`: List all listings
- `POST /api/listings/`: Create a new listing
- `GET /api/listings/<id>/`: Retrieve a listing
- `PUT /api/listings/<id>/`: Update a listing
- `DELETE /api/listings/<id>/`: Delete a listing

**Bookings:**
- `GET /api/bookings/`: List all bookings
- `POST /api/bookings/`: Create a new booking
- `GET /api/bookings/<id>/`: Retrieve a booking
- `PUT /api/bookings/<id>/`: Update a booking
- `DELETE /api/bookings/<id>/`: Delete a booking

### Swagger Documentation
Access the API documentation at http://127.0.0.1:8000/swagger/.

**Expected Responses:**
```
GET: 200 OK
POST: 201 Created
PUT: 200 OK
DELETE: 204 No Content
Errors (e.g., invalid data): 400 Bad Request
```


### Testing
Use Postman to test the endpoints

**1. Listings:**

**GET** `http://127.0.0.1:8000/api/listings/`: *Retrieve all listings*

**POST** `http://127.0.0.1:8000/api/listings/`:
```json
{
    "title": "Cozy Cabin",
    "description": "A nice cabin in the woods",
    "price": 100.00,
    "location": "Mountain Valley"
}
```

**GET** `http://127.0.0.1:8000/api/listings/1/`: *Retrieve a specific listing*

**PUT** `http://127.0.0.1:8000/api/listings/1/`:
```json
{
    "title": "Updated Cozy Cabin",
    "description": "A nice cabin in the woods",
    "price": 120.00,
    "location": "Mountain Valley"
}
```

**DELETE** `http://127.0.0.1:8000/api/listings/1/`: *Delete a listing*



**2. Bookings:**

**GET** `http://127.0.0.1:8000/api/bookings/`: *Retrieve all bookings*

**POST** `http://127.0.0.1:8000/api/bookings/`:
```json
{
    "listing": 1,
    "user": 1,
    "start_date": "2025-07-01",
    "end_date": "2025-07-05"
}
```

**GET** `http://127.0.0.1:8000/api/bookings/1/`: *Retrieve a specific booking*

**PUT** `http://127.0.0.1:8000/api/bookings/1/`:
```json
{
    "listing": 1,
    "user": 1,
    "start_date": "2025-07-02",
    "end_date": "2025-07-06"
}
```

**DELETE** `http://127.0.0.1:8000/api/bookings/1/`: *Delete a booking*
