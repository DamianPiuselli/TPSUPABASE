CREATE TABLE
    IF NOT EXISTS fact_wholesale (
        date date not null,
        item_code bigint not null,
        wholesale_price float not null,
        pk_wholesale int identity (1, 1) primary key
    );