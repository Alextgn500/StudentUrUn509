BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Users" (
	"id"	INTEGER,
	"username"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"age"	INT NOT NULL,
	"balance"	INT DEFAULT 1000,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (1,'Alex','alex@mail.com',25,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (2,'Maria','maria@mail.com',30,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (3,'John','john@mail.com',28,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (4,'Emma','emma@mail.com',22,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (5,'Michael','michael@mail.com',35,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (6,'Sarah','sarah@mail.com',27,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (7,'David','david@mail.com',33,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (8,'Lisa','lisa@mail.com',29,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (9,'James','james@mail.com',31,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (10,'Anna','anna@mail.com',26,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (11,'Irina','irina@mail.com',29,1000);
INSERT INTO "Users" ("id","username","email","age","balance") VALUES (12,'Sahsa','sa@mail.com',39,1000);
COMMIT;
