CREATE TABLE
    IF NOT EXISTS dim_category (
        category_code bigint primary key not null,
        category_name varchar(300) not null,
    );