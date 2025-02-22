CREATE TABLE meals(
    meal_id INTEGER PRIMARY KEY,
    meal_name TEXT NOT NULL UNIQUE,
    meal_cook_time TEXT,
    meal_prep_time TEXT,
    meal_complexity TEXT
)