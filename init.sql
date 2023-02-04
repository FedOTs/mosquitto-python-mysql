USE mqtt_data;

DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS user_to_client;
DROP TABLE IF EXISTS user_to_topics;

CREATE TABLE IF NOT EXISTS messages
(
    client_id varchar(255) not null,
    topic TEXT NOT NULL,
    payload TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    deleted_at DATETIME NULL,
    KEY(client_id, created_at)
);

CREATE TABLE IF NOT EXISTS user_to_client
(
    user_id int not null,
    client_id varchar(255) not null,
    created_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);

CREATE TABLE IF NOT EXISTS user_to_clientport
(
    user_id int not null,
    client_id varchar(255) not null,
    payload TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);