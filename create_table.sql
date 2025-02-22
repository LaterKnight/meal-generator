CREATE TABLE meals(
    meal_id int PRIMARY KEY,
    meal_name varchar(255) NOT NULL UNIQUE,
    meal_cook_time int,
    meal_prep_time int,
    meal_complexity varchar(255)
)