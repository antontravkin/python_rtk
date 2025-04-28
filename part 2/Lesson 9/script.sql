-- 1. Потери при работе с NULL значениями.
--
-- найти всех сотрудников, которые зарабатывают более 10000 и не получают комиссионных
select *
from employees e 
where salary > 5000 and comission_pct = 0;

select *
from employees e 
where salary > 5000 and coalesce(comission_pct,0) = 0;

-- 2. Ловушка NOT IN.
--
-- найти всех сотудников, которые являются руководителями в департаментах
select *
from employees e 
where e.employee_id in (select d.manager_id from departments d);

select *
from employees e 
where e.employee_id not in (select d.manager_id from departments d where manager_id is not null);

-- таких нет, давайте разбираться!
select val,
	val in (1,2) v1_1,
	val = 1 or val = 2 v1_2,
	val in (1,2,null) v2_1,
	val = 1 or val = 2 or val = null v2_2,
	val not in (1,2) v3_1,
	not (val = 1 or val = 2) v3_2,
	not (val = 1) and not (val = 2) v3_3,
	val not in (1,2,null) v4_1,
	not (val = 1) and not (val = 2) and not (val = null) v4_2
from (select generate_series(1,3) val) t;


-- 3.1. Вертикальное соединение
-- 
-- как по вашему в чем разница между UNION и UNION ALL?
select generate_series(1,6) val
union all
select generate_series(3,10) val
order by val;

select val from (
	select generate_series(1,3) val
	union
	select null val)
intersect
select val from (
	select generate_series(3,10) val
	union
	select null val);

select generate_series(1,3) val
except
select generate_series(3,10) val;


select *
from employees e 

-- self join:
-- найдите всех сотрудников и их непосрественных руководителей:
select e.first_name || ' ' || e.last_name emp,  m.first_name || ' ' || m.last_name manager
from employees e left join employees m
	on e.manager_id = m.employee_id 
	
-- что не так с этим запрсом?