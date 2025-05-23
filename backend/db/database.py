import os
from datetime import datetime
from dotenv import load_dotenv
from mongoengine import Document, StringField, DateTimeField
from motor.motor_asyncio import AsyncIOMotorClient  # Use AsyncIO MongoDB client
from decimal import Decimal
import json
from bson import ObjectId

# Load environment variables
load_dotenv()

# User model (if you're using it for authentication)
class User(Document):
    username = StringField(required=True, unique=True)
    name = StringField(required=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    meta = {'collection': 'users'}

# MongoDB async connection
client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client['360DegreeFitness']
profiles_collection = db['fitness_profiles']
changes_collection = db['fit_profile_changes']
key_recommendations_collection = db["key_recommendations"] # for chatbot to store key recommendations
conversation_history_collection = db["conversation_history"] # for chatbot to store conversation history
meal_diary_collection = db["meal_diary"] # for storing users' meal diary and meal logs
exercise_diary_collection = db["exercise_diary"] # for storing users' exercise diary and exercise logs
weight_diary_collection = db["weight_diary"] # for storing users' weight diary and weight logs
nutrition_goals_collection = db["nutrition_goals"]
fitness_plans_collection = db.get_collection("fitness_plans")

# Decimal handling
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

# Profile update functions
async def update_latest_profile(user_id, update_data):
    # Convert Decimal objects to float
    update_data = json.loads(json.dumps(update_data, cls=DecimalEncoder))
    update_data['updated_at'] = datetime.utcnow()
    await profiles_collection.update_one(
        {"user_id": user_id},
        {"$set": update_data},
        upsert=True
    )

async def log_profile_change(user_id, change_data):
    # Convert Decimal objects to float
    change_data = json.loads(json.dumps(change_data, cls=DecimalEncoder))
    change_data['user_id'] = user_id
    change_data['timestamp'] = datetime.utcnow()
    await changes_collection.insert_one(change_data)


# CRUD operations for meal diary
async def get_meal(user_id, date=None, start_date=None, end_date=None): # Used for retrieving meal logs within a date range.
    query = {"user_id": user_id}
    
    if date:
        query["date"] = date
    elif start_date and end_date:
        query["date"] = {"$gte": start_date, "$lte": end_date}
    
    return await meal_diary_collection.find(query).to_list(length=None)

async def update_meal_log(log_id, update_data): # Used for updating a meal log.
    update_data['updated_at'] = datetime.utcnow()
    await meal_diary_collection.update_one(
        {"_id": ObjectId(log_id)},
        {"$set": update_data}
    )

async def delete_meal_log(log_id): # Used for deleting a meal log.
    await meal_diary_collection.delete_one({"_id": ObjectId(log_id)})

# Setup indexes for all collections
async def setup_exercise_diary_indexes():
    """Create indexes for exercise diary collection"""
    try:
        # Drop all indexes except _id
        indexes = await exercise_diary_collection.list_indexes().to_list(length=None)
        for index in indexes:
            if index.get('name') != '_id_':  # Don't drop the _id index
                try:
                    await exercise_diary_collection.drop_index(index.get('name'))
                except Exception:
                    pass  # Silently continue if index drop fails
                
        # Create a compound index on user_id and date
        await exercise_diary_collection.create_index(
            [("user_id", 1), ("date", 1)],
            unique=True,
            name="user_id_date_unique"  # Give it a specific name
        )
    except Exception as e:
        print(f"Error setting up exercise diary indexes: {e}")

async def setup_weight_diary_indexes():
    """Create indexes for weight diary collection"""
    try:
        # Drop all indexes except _id
        indexes = await weight_diary_collection.list_indexes().to_list(length=None)
        for index in indexes:
            if index.get('name') != '_id_':  # Don't drop the _id index
                try:
                    await weight_diary_collection.drop_index(index.get('name'))
                except Exception:
                    pass  # Silently continue if index drop fails
                
        # Create a compound index on user_id and date
        await weight_diary_collection.create_index(
            [("user_id", 1), ("date", 1)],
            unique=True,
            name="user_id_date_unique"  # Give it a specific name
        )
    except Exception as e:
        print(f"Error setting up weight diary indexes: {e}")

async def setup_nutrition_goals_indexes():
    """Create indexes for nutrition goals collection"""
    try:
        # Drop all indexes except _id
        indexes = await nutrition_goals_collection.list_indexes().to_list(length=None)
        for index in indexes:
            if index.get('name') != '_id_':  # Don't drop the _id index
                try:
                    await nutrition_goals_collection.drop_index(index.get('name'))
                except Exception:
                    pass  # Silently continue if index drop fails
                
        # Create a unique index on user_id
        await nutrition_goals_collection.create_index(
            "user_id",
            unique=True,
            name="user_id_unique"  # Give it a specific name
        )
    except Exception as e:
        print(f"Error setting up nutrition goals indexes: {e}")

async def setup_meal_diary_indexes():
    """Create indexes for meal diary collection"""
    try:
        # Drop all indexes except _id
        indexes = await meal_diary_collection.list_indexes().to_list(length=None)
        for index in indexes:
            if index.get('name') != '_id_':  # Don't drop the _id index
                try:
                    await meal_diary_collection.drop_index(index.get('name'))
                except Exception:
                    pass  # Silently continue if index drop fails
                
        # Create a compound index on user_id and date
        await meal_diary_collection.create_index(
            [("user_id", 1), ("date", 1)],
            unique=True,
            name="user_id_date_unique"  # Give it a specific name
        )
    except Exception as e:
        print(f"Error setting up meal diary indexes: {e}")

# This function runs when your app starts (called from app.py)
# It ensures your database indexes are set up
async def init_db():
    try:
        # Quietly set up database indexes
        await setup_meal_diary_indexes()
        await setup_exercise_diary_indexes()
        await setup_weight_diary_indexes()
        await setup_nutrition_goals_indexes()
    except Exception as e:
        print(f"Error setting up database indexes: {e}")