
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
	"title" varchar(255) NOT NULL,
	"user_id" int NOT NULL,
	"ticket_status_id" int NOT NULL,
	"ticket_category_id" int NOT NULL,
	"created_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	"updated_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	"resolution_text" varchar(255),
	"closed_at" TIMESTAMPTZ,
	PRIMARY KEY("id")
);

CREATE INDEX "Ticket_index_0"
ON "Ticket" ("user_id");
CREATE INDEX "Ticket_index_1"
ON "Ticket" ("created_at");
CREATE INDEX "Ticket_index_2"
ON "Ticket" ("updated_at");
CREATE TABLE IF NOT EXISTS "TicketStatus" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255) NOT NULL UNIQUE,
	"is_closed" boolean NOT NULL DEFAULT false,
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

CREATE INDEX "Message_index_0"
ON "Message" ("ticket_id");
CREATE INDEX "Message_index_1"
ON "Message" ("created_at");
CREATE TABLE IF NOT EXISTS "TicketCategory" (
	"id" serial NOT NULL UNIQUE,
	"name" varchar(255) NOT NULL,
	PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "TicketStatusHistory" (
	"id" serial NOT NULL UNIQUE,
	"ticket_id" int NOT NULL,
	"from_status_id" int NOT NULL,
	"to_status_id" int NOT NULL,
	"changed_by_user_id" int NOT NULL,
	"changed_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	"comment" text,
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
ALTER TABLE "Ticket"
ADD FOREIGN KEY("ticket_category_id") REFERENCES "TicketCategory"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "TicketStatusHistory"
ADD FOREIGN KEY("ticket_id") REFERENCES "Ticket"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "TicketStatusHistory"
ADD FOREIGN KEY("from_status_id") REFERENCES "TicketStatus"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "TicketStatusHistory"
ADD FOREIGN KEY("to_status_id") REFERENCES "TicketStatus"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "TicketStatusHistory"
ADD FOREIGN KEY("changed_by_user_id") REFERENCES "User"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;