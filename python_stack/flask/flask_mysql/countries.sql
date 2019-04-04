use world;

select countries.name, languages.language, languages.percentage
from countries
join languages on countries.id	= languages.country_id
where languages.language = 'Slovene'
order by languages.percentage desc;

select countries.name, count(cities.name) as num_cities
from countries
join cities on countries.id = cities.country_id
group by countries.name
order by num_cities desc;

select cities.name, cities.population
from countries
join cities on countries.id = cities.country_id
where countries.name = 'Mexico'
order by cities.population desc;

select countries.name, languages.language, languages.percentage
from countries
left join languages on countries.id = languages.country_id
where languages.percentage >= 89
order by languages.percentage desc;

select name, surface_area, population
from countries
where surface_area < 501 and population > 100000
order by name desc;

select countries.name, countries.government_form, countries.capital, countries.life_expectancy
from countries
where government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

select countries.name, cities.name, cities.population, cities.district
from countries
left join cities on countries.id = cities.country_id
where cities.district = 'Buenos Aires' AND cities.population > 500000;

select region, count(name) as count
from countries
group by region
order by count desc;