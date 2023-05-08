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

/* object explorer da connect ile database i bağlıyoruz */

/* önceden luşturduğumuz "bct" database ini kullan diyoruz  */
use bct;

/* Bölümler tablosu oluşturduk  */

Create table bolumler(
  bolum_no int,
  bolum_adi nchar(50),
  primary key (bolum_no));  /* bolum_no kolonunu primary key olarak işaretledik ,"bolum_no int primary key" yazmakla aynı şey*/
  
/* ürünler  tablosu oluşturduk  */
Create table urunler(
  urun_no int primary key,
  urun_adi varchar(15),
  urun_sayisi int, 
  urun_fiyat decimal(18,2),
  bolum_no int,
  foreign key(bolum_no) references bolumler(bolum_no)); 

/* taloların içini doldurduk  */  
insert into bolumler values (1,'Beyaz eşya');
insert into bolumler values (2,'Bilgisayar');
insert into bolumler values (3,'TV');
insert into bolumler values (4,'Fotokamera');
insert into bolumler values (5,'Ses');
insert into bolumler values (6,'Telefon');

insert into urunler values (1,'Notebook',3,2300.00,2);
insert into urunler values (2,'Ultrabook',5,3000.00,2);
insert into urunler values (3,'USB Bellek',7,20.00,2);
insert into urunler values (4,'Harici Disk',4,180.00,2);
insert into urunler values (5,'Apple Tablet',4,1000.00,2);
insert into urunler values (6,'Android Tablet',6,800.00,2);
insert into urunler values (7,'windows Tablet',6,999.99,2);
insert into urunler values (8,'Digital kamera',10,600.00,4);
insert into urunler values (9,'Profosyonel kamera',6,1600.00,4);
insert into urunler values (10,'Buzdolabı',5,1200.00,1);
insert into urunler values (11,'Bulaşık Mak.',5,900.00,1);
insert into urunler values (12,'LCD',4,400.00,3);
insert into urunler values (13,'Apple Telefon',5,40000.00,6);
insert into urunler values (14,'Android Telefon',10,4000.00,6);
insert into urunler values (15,'stero hoparlör',5,400.00,5);
insert into urunler values (16,'5+1 sistem',10,1000.00,5);
insert into urunler values (17,'plazma TV',6,4400.00,3);
insert into urunler values (18,'İşlemci',9,200.00,2);


/* bolum_no larına göre , her bölümde toplam kaç ürün var */  
select bolum_no , sum(urun_sayisi) as toplam_urun_sayisi from urunler group by bolum_no

/* bolum_no larına göre , her bölümde toplam kaç ürün var ama ana tabloda urin fiyatı >600 olanları aldık ve toplam ürün sayısı >10 olanları select ile gösterdik */  

/* where --> ana tablodaki veri için çalışır
/* having --> select ile getirdiğimiz tabloda çalışır  */  
select bolum_no , sum(urun_sayisi) as toplam_urun_sayisi from urunler where urun_fiyat>600 group by bolum_no having toplam_urun_sayisi>10

/* üst select sorgusu 
bir önceki sorguyu t1 olarak tanımladık ve bu şekilde select ile çağırdığımız zaman "having" kullanmamıza gerek kalmadı  */ 

select t1. * from
(select bolum_no , sum(urun_sayisi) as toplam_urun_sayisi from urunler group by bolum_no) t1
where toplam_urun_sayisi>15

/* ürün fiyatı en yüksek 5 i sıralı şekilde gösterdik */
select top(5) urun_fiyat from urunler order by urun_fiyat desc ;

/* farklı kaç tane girdi var */
select distinct bolum_no from urunler;

/* Join */
/* bölümler tablosundaki her bir "bölüm_adi" kolonundan , "ürünler" tablosunda kaç tane var */
select Bolumler.bolum_adi,t2.toplam from bolumler left join /* bolum adını ve toplam sayıyı yazdıracağız , left join dediğimiz için ilek tabloya ikinciyi bağladık */
(select bolum_no , sum(urun_sayisi) as toplam from urunler group by bolum_no) t2 on Bolumler.bolum_no=t2.bolum_no /* select i t2 olarak alias verdik , ikinci tablomuz oldu , 
"on"* ile  iki key i birbirine eşleştirdik /

/*	A left join B	--> A tablosuna B yi joinle
	A right join B	--> B tablosuna A yı joinle
	A inner join B  --> A ile B nin kesişimini 
	A outer join B	--> A ile B nin hepsini getirir , kesişenler yan yana , kesişmeyenleri de boş (N/A) olarak getirir. 
*/

select * from
(select t1.*,t2.toplam from bolumler t1 left join 
(select bolum_no , sum(urun_sayisi) as toplam from urunler group by bolum_no) t2 on t1.bolum_no=t2.bolum_no) t3
where toplam>15
