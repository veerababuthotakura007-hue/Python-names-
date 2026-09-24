/* Write your PL/SQL query statement below */
select C.name as  Customers from
customers C  left join orders O
on C.id=o.customerID
where o.id is null;