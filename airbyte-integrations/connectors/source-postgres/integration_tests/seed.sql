ALTER ROLE postgres WITH REPLICATION;

CREATE
    TABLE
        id_and_name(
            id INTEGER,
            name VARCHAR(200)
        );

INSERT
    INTO
        id_and_name(
            id,
            name
        )
    VALUES(
        1,
        'picard'
    ),
    (
        2,
        'crusher'
    ),
    (
        3,
        'vash'
    );

select pg_create_logical_replication_slot('debezium_slot', 'pgoutput')
;

CREATE
    PUBLICATION publication FOR ALL TABLES;
