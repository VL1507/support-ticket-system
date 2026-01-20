CREATE TABLE IF NOT EXISTS "User" (
	"id" UUID NOT NULL UNIQUE,
	"name" VARCHAR(255) NOT NULL,
	"login" VARCHAR(255) NOT NULL UNIQUE,
	"hash_password" VARCHAR(255) NOT NULL,
	"role_id" INTEGER NOT NULL,
	"is_active" BOOLEAN NOT NULL DEFAULT true,
	PRIMARY KEY("id")
);




CREATE TABLE IF NOT EXISTS "Role" (
	"id" SERIAL NOT NULL UNIQUE,
	"name" VARCHAR(255) NOT NULL UNIQUE,
	PRIMARY KEY("id")
);




CREATE TABLE IF NOT EXISTS "Ticket" (
	"id" UUID NOT NULL UNIQUE,
	"title" VARCHAR(255) NOT NULL,
	"user_id" UUID NOT NULL,
	"ticket_status_id" INTEGER NOT NULL,
	"ticket_category_id" INTEGER NOT NULL,
	"created_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	"updated_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	"resolution_text" TEXT,
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
	"id" SERIAL NOT NULL UNIQUE,
	"name" VARCHAR(255) NOT NULL UNIQUE,
	"is_closed" BOOLEAN NOT NULL DEFAULT false,
	PRIMARY KEY("id")
);




CREATE TABLE IF NOT EXISTS "Message" (
	"id" SERIAL NOT NULL UNIQUE,
	"ticket_id" UUID NOT NULL,
	"text" TEXT NOT NULL,
	"created_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	"user_id" UUID NOT NULL,
	PRIMARY KEY("id")
);


CREATE INDEX "Message_index_0"
ON "Message" ("ticket_id");
CREATE INDEX "Message_index_1"
ON "Message" ("created_at");

CREATE TABLE IF NOT EXISTS "TicketCategory" (
	"id" SERIAL NOT NULL UNIQUE,
	"name" VARCHAR(255) NOT NULL,
	PRIMARY KEY("id")
);




CREATE TABLE IF NOT EXISTS "TicketStatusHistory" (
	"id" SERIAL NOT NULL UNIQUE,
	"ticket_id" UUID NOT NULL,
	"from_status_id" INTEGER NOT NULL,
	"to_status_id" INTEGER NOT NULL,
	"changed_by_user_id" UUID NOT NULL,
	"changed_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	"comment" TEXT,
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