CREATE TABLE IF NOT EXISTS station_log (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    station_id INTEGER NOT NULL,
    available_bikes INTEGER NOT NULL,
    empty_docks INTEGER NOT NULL,
    crawl_date TEXT NOT NULL,
    FOREIGN KEY(station_id) REFERENCES station(id)
);