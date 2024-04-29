CREATE TABLE IF NOT EXISTS postgres_db.public.t_test (
    ID serial PRIMARY KEY,
    DATA TEXT NOT NULL,
    DATE date NOT NULL
);