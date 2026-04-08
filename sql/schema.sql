CREATE TABLE indicators (
    id SERIAL PRIMARY KEY,
    indicator_name VARCHAR(255) NOT NULL,
    value NUMERIC(15, 2) NOT NULL,
    year INTEGER NOT NULL,
    source VARCHAR(255),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
