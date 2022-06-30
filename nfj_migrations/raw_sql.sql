create table companies(
    company_id SERIAL primary key,
    name text not null,
    url text not null,
    UNIQUE (name, url)
);

-- put create and (rollback) delete scripts for the whole DB here