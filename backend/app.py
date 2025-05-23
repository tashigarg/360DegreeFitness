from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .db.connection import Database
from .db.database import init_db
from .routers import userFitnessProfileRouter, fitnessPlanRouter, authRouter, chatRouter, mealLoggerRouter, nutritionGoalRouter, caloriesTrackerRouter, exerciseLoggerRouter, weightLoggerRouter

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",    # Local React app
        "http://127.0.0.1:3000",    # Alternative local URL
        "http://client:3000",       # Docker service name
        "http://server:5050",       # Server service in Docker
        "http://localhost:5050",    # Local server
        "http://127.0.0.1:5050"     # Alternative local server URL
    ],  # Your React app URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_db_client():
    await Database.connect_db()
    await init_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    await Database.close_db()

# Include routers
app.include_router(authRouter.auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(
    userFitnessProfileRouter.profile_router,
    tags=["Fitness Profile"]
)
app.include_router(fitnessPlanRouter.plan_router)
app.include_router(
    chatRouter.chat_router,
    tags=["Chat"]
)
app.include_router(
    mealLoggerRouter.meal_log_router,
    tags=["Meal Logger"]
)
app.include_router(
    nutritionGoalRouter.nutrition_goal_router,
    tags=["Nutrition Goals"]
)
app.include_router(
    caloriesTrackerRouter.calorie_tracker_router,
    tags=["Calorie Tracker"]
)
app.include_router(
    exerciseLoggerRouter.exercise_log_router,
    tags=["Exercise Logger"]
)
app.include_router(
    weightLoggerRouter.weight_log_router,
    tags=["Weight Logger"]
)

# Data model for analysis input
class DataAnalysisInput(BaseModel):
    numbers: list[float]  # Example: List of numbers to analyze

# Endpoint for data analysis
@app.post("/api/analyze")
async def analyze_data(input: DataAnalysisInput):
    """
    Perform data analysis and return the results.
    """
    numbers = input.numbers
    average = sum(numbers) / len(numbers) if numbers else 0
    return {"average": average, "count": len(numbers)}

# is user profile existing & completed?
# create a fitness profile for the user
# get user fitness profile
# edit user fitness profile
# delete user fitness profile
# create fitness plan
# get fitness plan
# delete fitness plan


