USE twitter;

select * from users;

insert into users (first_name, last_name, handle, birthday, created_at, updated_at)
values('Scott','Aubuchon','BigRon',10/23/1986,NOW(), NOW());

update users
set handle = 'MassiveRon'
where id = 6;

delete from users
where id = 6;