use survey;


insert into  location (locale, created_at, updated_at)
Values ('DC', now(), now()),
('Seattle', now(), now()),
('Mars, lolz', now(), now());

insert into language (lang, created_at, updated_at)
values ('Python', now(), now()),
('Arabic', now(), now()),
('VBA? Srsly?', now(), now());

insert into sex (sex, created_at, updated_at)
values ('Male', now(), now()),
('Female', now(), now()),
('Nah', now(), now());

insert into ninja (language_id, location_id, sex_id, name, comment, subscribe, create_at, updated_at)
values((select id from language where lang = 'Python'), (select id from location where locale = 'DC'), (select id from sex where sex = 'Male'), 'Scott', 'None', TRUE, now(), now());

select ninja.name, ninja.comment, ninja.subscribe, max(ninja.id), language.lang, location.locale, sex.sex 
from ninja as ninja
left join location on ninja.location_id = location.id
left join language on ninja.language_id = language.id
left join sex on ninja.sex_id = sex.id
group by ninja.id;