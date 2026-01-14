
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


CREATE TABLE IF NOT EXISTS "Ticket" (
	"id" serial NOT NULL UNIQUE,
	"ticket_status_id" int NOT NULL,
	"user_id" int NOT NULL,
	"created_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "TicketStatus" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "Message" (
	"id" serial NOT NULL UNIQUE,
	"ticket_id" int NOT NULL,
	"text" text NOT NULL,
	"created_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	"user_id" int NOT NULL,
	PRIMARY KEY("id")
);


ALTER TABLE "User"
ADD FOREIGN KEY("role_id") REFERENCES "Role"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Ticket"
ADD FOREIGN KEY("ticket_status_id") REFERENCES "TicketStatus"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Ticket"
ADD FOREIGN KEY("user_id") REFERENCES "User"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Message"
ADD FOREIGN KEY("ticket_id") REFERENCES "Ticket"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Message"
ADD FOREIGN KEY("user_id") REFERENCES "User"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;