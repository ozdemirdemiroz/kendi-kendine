/* database oluşturma */

CREATE DATABASE bct;

/* tablo oluşturma*/
use bct;

Create table member(
    id int primary key,
    ad varchar(15),
    soyad varchar(15), 
    yas int); 

/* tablo içine değerler girme*/
/*                        (id,ad    , soyad  , yaş) */
insert into Member values (3,'ahmet','güngör',39);
insert into Member values (4,'yasin','güngör',39);

/*tabloda yeni kolon açma /silme */
ALTER TABLE member
ADD maas int;
drop COLUMN silinecek_kolon

/*tablodaki verileri güncelleme*/
update member set yas=27 where ad='ozdemir';  
update member set bolum='c' where id>6 and id<10;

/*veri silme*/
delete from member where id=6;

/*tabloyu silme*/
drop table member;

/* tabloyu dökme*/

select ad,yas from member; /* tablonun ad ve yaş kolonlarını döker*/
select * from member/* tablonun ad ve yaş kolonlarını döker*/
select * from member where ad like ('%a%');
select * from member order by maas ASC /* maaşa göre sıralı döküm aldık */
select bolum , avg(maas) as mass_ort from member group by bolum /* her bölümün maaş ortalamasını döktük */