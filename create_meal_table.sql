-- Creates the main "meals" table. You will need to run this first to set up the table(s) before you can run the program.
CREATE TABLE meals(
    meal_id INTEGER PRIMARY KEY,
    meal_name TEXT NOT NULL UNIQUE,
    meal_cook_time TEXT,
    meal_prep_time TEXT,
    meal_complexity TEXT
)