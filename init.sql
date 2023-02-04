USE mqtt_data;

DROP TABLE IF EXISTS messages;

CREATE TABLE IF NOT EXISTS messages
(
    client_id varchar(255) not null,
    topic TEXT NOT NULL,
    payload TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    deleted_at DATETIME NULL,
    KEY(client_id, created_at)
);
