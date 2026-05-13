CREATE TABLE folders (
    id SERIAL,
    parent_id INTEGER,
    name VARCHAR(60) NOT NULL,
    created_at TIMESTAMP DEFAULT current_timestamp,
    modified_at TIMESTAMP DEFAULT current_timestamp,
    deleted BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (id),
    CONSTRAINT fk_parent
    FOREIGN KEY (parent_id)
    REFERENCES folders (id)
);
