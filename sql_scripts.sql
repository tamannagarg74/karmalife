
create table user_level_info (
signup date,
KYC date,
`UNLOCK` date,
first_transaction_date date,
last_transaction_date date,
partner_id varchar(255) NOT NULL UNIQUE,
user_id varchar(255) NOT NULL UNIQUE
);

insert into user_level_info values (
'2022-04-22', '2022-04-23', '2022-04-23', '2022-04-23', '2022-04-30', '0123', 'ABCD');

insert into user_level_info values (
'2022-04-27', '2022-04-27', '2022-04-28', '2022-04-28', '2022-05-10', '1234', 'BCDE');


insert into user_level_info values (
'2022-04-27', '2022-04-27', '2022-04-28', '2022-04-28', '2022-04-30', '2345', 'CDEF');

insert into user_level_info values (
'2021-08-20', '2021-08-20', '2021-08-23', '2021-08-24', '2022-08-30', '3456', 'ADEF');

insert into user_level_info values (
'2021-09-15', '2021-09-15', '2021-09-23', '2021-09-24', '2022-09-30', '4567', 'ABEF');

create table db_event.de_events_op (
event_date date,
event_timestamp timestamp,
inititied_by bool,
partner_id varchar(255) NOT NULL UNIQUE,
utm_medium varchar(255),
utm_campaign varchar(255),
unique_users_coming_to_web int,
unique_users_coming_to_web_list varchar(255),
unique_users_installed int,
unique_users_installed_list varchar(255)
);

insert into db_event.de_events_op values(
'2022-04-20', '2022-04-20 02:20:20.126', True, '0123', 'SMS', 'Holi_bonanza', 100000, '[ABCD, BCDE]', 50000, '[ABCD]'
);

insert into db_event.de_events_op values(
'2022-04-22', '2022-04-22 08:10:19.170', True, '1234', 'SMS', 'Holi_bonanza', 100000, '[ABCD]', 80000, '[ABCD, BCDE]'
);

insert into db_event.de_events_op values(
'2022-04-27', '2022-04-27 11:21:19.149', True, '2345', 'Whatsapp', 'Holi_bonanza', 100000, '[ABCD]', 40000, '[ABCD, BCDE]'
);

insert into db_event.de_events_op values(
'2021-08-20', '2021-08-20 11:21:19.149', True, '3456', 'Whatsapp', 'Diwali_campaign', 80000, '[CDEF]', 50000, '[BCDE]'
);

insert into db_event.de_events_op values(
'2021-09-15', '2021-09-15 11:21:19.149', False, '4567', 'Whatsapp', 'Diwali_campaign', 20000, '[CDEF, BCDE]', 10000, '[ABCD]'
);