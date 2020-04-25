select name from employees
where id not in (select managerId from employees WHERE managerId is not null);
