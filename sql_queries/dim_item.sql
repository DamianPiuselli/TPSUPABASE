CREATE TABLE
    IF NOT EXISTS dim_item (
        item_code bigint primary key not null,
        item_name varchar(300) not null,
        loss_rate float null category_code bigint not null,
    );