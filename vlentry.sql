23 = Jaslene
58 = Janani
60 = Dheeraj
27 = Sripadma 
insert into Vineland VALUES (23,23,1), (58,58,1), (60,60,1);

insert into VL0 VALUES (23,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), (58,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(60,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1);

insert into VL1 VALUES (23,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1), (58,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1),(60,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1);

insert into VL2 VALUES(23,1,1,1,1,1,1,1,1,1,1),(58,1,1,1,1,1,1,1,1,1,1),(60,1,1,1,1,1,1,1,1,1,1);

insert into VL3 VALUES (23,1,1,1,1,1,1),(58,1,1,1,1,1,1),(60,1,1,1,1,1,1);

insert into VL4 VALUES (23,1,1,1,1,1,1),(58,1,1,1,1,1,1),(60,1,1,1,1,1,1);

insert into VL5 VALUES (23,1,1,1,1,0), (58,0,1,1,0,0), (60,0,1,1,0,0);

insert into VL6 VALUES (23,1,1,1,1), (58,1,1,1,1), (60,1,1,1,1);

insert into VL7 VALUES (23,1,1,0,1,1), (58,0,1,0,0,1), (60,0,1,0,0,1);

insert into VL8 values (23,1,1,1,1),(58,1,1,0,1),(60,1,1,0,1);

insert into VL9 values (23,1,1,1), (58,1,1,1), (60,1,1,1);




create view Combined as select * from child C NATURAL JOIN (RPM R NATURAL JOIN (DST D NATURAL JOIN (BST B NATURAL JOIN (GDT NATURAL JOIN Vineland V)))); 


select * from child C NATURAL JOIN (RPM R NATURAL JOIN (DST D NATURAL JOIN (BST B NATURAL JOIN (GDT NATURAL JOIN Vineland V))))
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';