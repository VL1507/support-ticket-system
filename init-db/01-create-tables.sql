
CREATE TABLE IF NOT EXISTS "User" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255) NOT NULL,
	"login" varchar(255) NOT NULL,
	"hash_password" varchar(255) NOT NULL,
	"role_id" int NOT NULL,
	PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "Role" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "Tiket" (
	"id" serial NOT NULL UNIQUE,
	"tiket_status_id" int NOT NULL,
	"user_id" int NOT NULL,
	"created_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "TiketStatus" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "Message" (
	"id" serial NOT NULL UNIQUE,
	"tiket_id" int NOT NULL,
	"text" text NOT NULL,
	"created_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	"user_id" int NOT NULL,
	PRIMARY KEY("id")
);


ALTER TABLE "User"
ADD FOREIGN KEY("role_id") REFERENCES "Role"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Tiket"
ADD FOREIGN KEY("tiket_status_id") REFERENCES "TiketStatus"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Tiket"
ADD FOREIGN KEY("user_id") REFERENCES "User"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Message"
ADD FOREIGN KEY("tiket_id") REFERENCES "Tiket"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Message"
ADD FOREIGN KEY("user_id") REFERENCES "User"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;