# California Housing Price Prediction API
https://california-housing-prediction-docker.onrender.com
A machine learning project that predicts California housing prices using the **California Housing dataset** from Scikit-learn. The trained Random Forest model is saved as a Pickle file and deployed as a REST API using **FastAPI, Docker, GitHub, and Render**.

## Project Workflow

```text
California Housing Dataset
          ↓
Data Preprocessing
          ↓
Random Forest Regression
          ↓
Trained Model
          ↓
house_price_model.pkl
          ↓
FastAPI
          ↓
Docker
          ↓
GitHub
          ↓
Render
          ↓
Live Prediction API
```

## Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- FastAPI
- Uvicorn
- Pickle
- Docker
- GitHub
- Render

## Dataset

The project uses the **California Housing dataset** available through Scikit-learn.

The dataset contains 8 input features:

| Feature | Description |
|---|---|
| `MedInc` | Median income in the block |
| `HouseAge` | Median house age |
| `AveRooms` | Average number of rooms |
| `AveBedrms` | Average number of bedrooms |
| `Population` | Block population |
| `AveOccup` | Average house occupancy |
| `Latitude` | Geographic latitude |
| `Longitude` | Geographic longitude |

The target variable represents the median house value in units of **$100,000**.

## Machine Learning Model

A **Random Forest Regressor** is used for prediction.

Example configuration:

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
```

The trained model is saved using Python Pickle:

```python
with open("model/house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)
```

## Project Structure

```text
california-housing-api/
│
├── model/
│   └── house_price_model.pkl
│
├── app.py
├── train.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Running Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd california-housing-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run FastAPI

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### GET `/`

Checks whether the API is running.

Example response:

```json
{
  "message": "California Housing Price Prediction API is running"
}
```

### GET `/health`

Health check endpoint.

Example response:

```json
{
  "status": "healthy"
}
```

### POST `/predict`

Predicts the house price based on the supplied housing features.

Example request:

```json
{
  "MedInc": 8.3,
  "HouseAge": 25,
  "AveRooms": 6.2,
  "AveBedrms": 1.1,
  "Population": 1500,
  "AveOccup": 3.0,
  "Latitude": 34.2,
  "Longitude": -118.4
}
```

Example response:

```json
{
  "predicted_price": 4.52,
  "predicted_price_usd": 452000.0
}
```

The exact prediction may vary depending on the trained model.

## Docker

The application is containerized using Docker.

### Build the Docker image

```bash
docker build -t california-housing-api .
```

### Run the Docker container

```bash
docker run -p 8000:8000 california-housing-api
```

The API can then be accessed at:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

## Deployment

The application is deployed using **Render**.

Deployment workflow:

```text
GitHub Repository
       ↓
Dockerfile
       ↓
Render
       ↓
Docker Container
       ↓
FastAPI
       ↓
Live API
```

### Live API

**Render URL:**  
`<YOUR_RENDER_URL>`

### Swagger Documentation

**Swagger URL:**  
`<YOUR_RENDER_URL>/docs`

## Logging and Monitoring

Render logs are used to monitor the deployed FastAPI application.

The logs can be checked from the Render dashboard to verify:

- Docker image build
- Application startup
- Uvicorn server status
- API requests
- Application errors

## Testing

The `/predict` endpoint was tested using FastAPI Swagger UI.

Testing workflow:

```text
Input Housing Features
        ↓
POST /predict
        ↓
FastAPI
        ↓
Pickle Model
        ↓
Random Forest Prediction
        ↓
Predicted House Price
```

## Learning Outcomes

This project demonstrates an end-to-end machine learning deployment workflow:

- Loading a dataset using Scikit-learn
- Training a machine learning regression model
- Evaluating the model
- Saving a trained model using Pickle
- Building a REST API using FastAPI
- Testing an API using Swagger UI
- Containerizing the application using Docker
- Version controlling the project using GitHub
- Deploying the application using Render
- Checking application logs and monitoring deployment status

## Author

**Joshva Patrick**

Computer Science Engineering Student  
Data Science / Machine Learning
