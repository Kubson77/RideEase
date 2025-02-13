-- auto-generated definition
create table first_name
(
    id   int auto_increment
        primary key,
    name varchar(15) not null
);

create table last_name
(
    id   int auto_increment
        primary key,
    name varchar(15) not null
);

create table car_model
(
    id   int auto_increment
        primary key,
    name varchar(15) not null
);

create table car_brand
(
    id   int auto_increment
        primary key,
    name varchar(15) not null
);

create table customer
(
    id             int auto_increment
        primary key,
    first_name     int         not null,
    last_name      int         not null,
    licence_number varchar(20) null,
    constraint customer_ibfk_1
        foreign key (first_name) references first_name (id)
            on update cascade,
    constraint customer_ibfk_2
        foreign key (last_name) references last_name (id)
            on update cascade
);

create index first_name
    on customer (first_name);

create index last_name
    on customer (last_name);

create table car
(
    id           int auto_increment
        primary key,
    brand_id     int         not null,
    model_id     int         not null,
    plate_number varchar(10) not null,
    constraint car_ibfk_1
        foreign key (brand_id) references car_brand (id)
            on update cascade,
    constraint car_ibfk_2
        foreign key (model_id) references car_model (id)
            on update cascade
);

create index brand_id
    on car (brand_id);

create index model_id
    on car (model_id);

create table rent_car
(
    id          int auto_increment
        primary key,
    car_id      int  not null,
    customer_id int  not null,
    rented_on   date not null,
    returned_on date null,
    constraint rent_car_ibfk_1
        foreign key (car_id) references car (id)
            on update cascade,
    constraint rent_car_ibfk_2
        foreign key (customer_id) references customer (id)
            on update cascade
);

create index car_id
    on rent_car (car_id);

create index customer_id
    on rent_car (customer_id);
