
# Travel Backend API with FastAPI and Django

This project implements a travel backend using Django and FastAPI, providing RESTful APIs for itineraries and recommendations. The project integrates Django ORM with FastAPI to expose itinerary data through well-structured endpoints, while ensuring scalability and smooth data serialization. 

## Project Setup

1. **Project Structure**:
   - The project is divided into **Django** and **FastAPI** components. 
   - **Django** is used for managing models and admin interfaces.
   - **FastAPI** is utilized for exposing RESTful APIs that interact with the Django models.

2. **Initialization**:
   - A project named `travel_backend` is created with an app `itineraries` to manage database models and administrative tasks.
   - A FastAPI file is initialized to expose RESTful APIs for itinerary management and recommendations.
   - Django settings are configured to work with FastAPI using `django.setup()`.

## Model Design

1. **Django Models**:
   - Defined models for **Hotel**, **Itinerary**, **Day**, **Transfer**, and **Activity**.
   - These models represent various aspects of a travel itinerary and associated entities like hotels, activities, and transfers.

2. **Serializers**:
   - Created Pydantic serializers to serialize Django models, ensuring smooth data exchange between FastAPI and Django.
   - Used Pydantic’s `orm_mode = True` to convert Django ORM querysets to Pydantic models.

3. **Seeding Data**:
   - Wrote a script to seed data for hotels (e.g., Phuket and Krabi) with 5-night stays, assigning activities for each day.

## API Development and MCP Server

1. **FastAPI Endpoints**:
   - Created endpoints for itineraries and recommendations, allowing users to create itineraries, retrieve a list of itineraries, and filter itineraries based on the number of nights.
   - APIs are built using FastAPI, making them fast and scalable.

2. **MCP Server**:
   - Exposed FastAPI endpoints while integrating with Django models. 
   - Used **Pydantic schemas** to serialize data from Django models, ensuring clean and consistent API responses.

## Testing

1. **Unit Tests**:
   - Implemented unit tests using **pytest** and FastAPI’s `TestClient` to ensure that the API endpoints function correctly.
   - Tests include the validation of response data, status codes, and API behavior under different conditions.

2. **Load Testing**:
   - Wrote a **Locust** script to simulate load on the itineraries endpoint, allowing performance testing and ensuring that the system can handle real-world traffic.

## Key Decisions and Assumptions

1. **Separation of Django and FastAPI**:
   - The project was structured by separating Django’s models/admin and FastAPI for better scalability and maintainability.
   
2. **Use of Pydantic**:
   - **Pydantic (orm_mode = True)** was used to serialize Django querysets smoothly, avoiding common serialization issues.

3. **Shared Environment**:
   - Both Django and FastAPI are deployed in the same environment with shared access to models and settings, ensuring seamless interaction between the two.

## Challenges and Solutions

1. **Integrating Django ORM into FastAPI**:
   - **Solution**: Used `django.setup()` and `os.environ` to load Django settings into FastAPI, allowing FastAPI to interact with Django’s ORM.

2. **Serializing Django Model with Pydantic**:
   - **Solution**: Enabled `orm_mode = True` in Pydantic models to avoid issues with converting Django models to Pydantic-compatible formats.

3. **Isolating Environments During Testing**:
   - **Solution**: Used separate **pytest** test cases and **TestClient** for modular testing, ensuring isolation between Django’s models and FastAPI’s routes.

4. **Managing Circular Imports**:
   - **Solution**: Carefully structured the project files to separate schemas, endpoints, and database logic. This ensured there were no circular import issues during the setup.

## Getting Started

1. **Clone the Repository**:
   Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/yourusername/travel-backend.git
   cd travel-backend
   ```

2. **Set Up Virtual Environment**:
   It is recommended to use a virtual environment for dependency management.
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the necessary dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   Run Django migrations to set up the database schema.
   ```bash
   python manage.py migrate
   ```

5. **Start FastAPI Server**:
   To start the FastAPI server, use:
   ```bash
   uvicorn fastapi_app:app --reload
   ```

   The server will be running at `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Conclusion

This project demonstrates the power of combining Django’s ORM and admin capabilities with FastAPI’s high-performance RESTful API features. The result is a scalable and maintainable solution for managing travel itineraries and generating recommendations.

For more information or contributions, please visit the [GitHub repository](https://github.com/krakesh1309/Travel-Itinerary-Management-Backend).

