BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Products" (
	"id"	INT,
	"title"	TEXT NOT NULL,
	"description"	TEXT,
	"price"	INT NOT NULL,
	"image_path"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
INSERT INTO "Products" ("id","title","description","price","image_path") VALUES (1,'Продукт1','Натуральный комплекс для ускорения метаболизма',400,'files/prod1.png');
INSERT INTO "Products" ("id","title","description","price","image_path") VALUES (2,'Продукт2','Пищевые волокна для контроля аппетита',600,'files/prod2.png');
INSERT INTO "Products" ("id","title","description","price","image_path") VALUES (3,'Продукт3','Витаминный комплекс с L-карнитином',800,'files/prod3.png');
INSERT INTO "Products" ("id","title","description","price","image_path") VALUES (4,'Продукт4','Протеиновый коктейль для снижения веса',1000,'files/prod4.png');
COMMIT;
