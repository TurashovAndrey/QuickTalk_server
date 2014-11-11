CREATE TABLE job_advert
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  title VARCHAR(255) NOT NULL,
  description VARCHAR(255),
  type_id integer NOT NULL,
  group_id integer NOT NULL,
  created_by character varying(64) NOT NULL,
  updated_by character varying(64),
  status_id integer NOT NULL,
  CONSTRAINT job_advert_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_advert
  OWNER TO job;

CREATE UNIQUE INDEX job_advert_advert_id_idx ON job_advert(advert_id);

-- advert locations table
CREATE TABLE job_advert_locations
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  location VARCHAR(255),
  CONSTRAINT job_advert_locations_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_advert_locations
  OWNER TO job;

CREATE TABLE job_advert_groups
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  group_id integer NOT NULL,
  CONSTRAINT job_advert_groups_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_advert_groups
  OWNER TO job;

CREATE TABLE job_advert_user_groups
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  group_id integer NOT NULL,
  user_id character varying(64) NOT NULL,
  CONSTRAINT job_advert_user_groups_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_advert_user_groups
  OWNER TO job;

CREATE TABLE job_statuses
(
  id serial NOT NULL,
  status VARCHAR(255),
  CONSTRAINT job_statuses_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_statuses
  OWNER TO job;

CREATE TABLE job_advert_statuses
(
  id serial NOT NULL,
  advert_id integer NOT NULL,
  status_id integer NOT NULL,
  CONSTRAINT job_advert_statuses_pkey PRIMARY KEY (id),
  CONSTRAINT job_advert_status_id_fkey FOREIGN KEY (status_id)
      REFERENCES job_statuses (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE job_advert_statuses
  OWNER TO job;

CREATE TABLE job_group
(
  id serial NOT NULL,
  group_name character varying(255) NOT NULL,
  CONSTRAINT job_group_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_group
  OWNER TO job;

CREATE TABLE job_advert_types
(
  id serial NOT NULL,
  category_id integer NOT NULL,
  type_name VARCHAR(255),
  CONSTRAINT job_advert_types_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_advert_types
  OWNER TO job;

CREATE TABLE job_advert_categories
(
  id serial NOT NULL,
  category_name VARCHAR(255),
  CONSTRAINT job_advert_categories_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_advert_categories
  OWNER TO job;

ALTER TABLE job_advert_types
    ADD CONSTRAINT job_advert_types_category_id_fkey FOREIGN KEY (category_id) REFERENCES job_advert_categories(id);

ALTER TABLE job_advert
    ADD CONSTRAINT job_advert_type_id_fkey FOREIGN KEY (type_id) REFERENCES job_advert_types(id);

ALTER TABLE job_advert
    ADD CONSTRAINT job_advert_group_id_fkey FOREIGN KEY (group_id) REFERENCES job_group(id);

ALTER TABLE job_advert
    ADD CONSTRAINT job_advert_created_by_fkey FOREIGN KEY (created_by) REFERENCES job_user(user_id);

ALTER TABLE job_advert
    ADD CONSTRAINT job_advert_updated_by_fkey FOREIGN KEY (updated_by) REFERENCES job_user(user_id);

ALTER TABLE job_advert
    ADD CONSTRAINT job_advert_status_id_fkey FOREIGN KEY (status_id) REFERENCES job_statuses(id);

ALTER TABLE job_advert_locations
    ADD CONSTRAINT job_advert_locations_advert_id_fkey FOREIGN KEY (advert_id) REFERENCES job_advert(advert_id);

ALTER TABLE job_advert_groups
    ADD CONSTRAINT job_advert_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES job_group(id);

ALTER TABLE job_advert_groups
    ADD CONSTRAINT job_advert_groups_advert_id_fkey FOREIGN KEY (advert_id) REFERENCES job_advert(advert_id);

ALTER TABLE job_advert_user_groups
    ADD CONSTRAINT job_advert_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES job_group(id);

ALTER TABLE job_advert_user_groups
    ADD CONSTRAINT job_advert_user_groups_advert_id_fkey FOREIGN KEY (advert_id) REFERENCES job_advert(advert_id);

ALTER TABLE job_advert_user_groups
    ADD CONSTRAINT job_advert_user_groups_user_id_fkey FOREIGN KEY (user_id) REFERENCES job_user(user_id);

