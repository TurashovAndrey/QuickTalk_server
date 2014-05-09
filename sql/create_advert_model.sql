CREATE TABLE leasing_advert
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
  CONSTRAINT leasing_advert_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_advert
  OWNER TO leasing;

CREATE UNIQUE INDEX leasing_advert_advert_id_idx ON leasing_advert(advert_id);

-- advert locations table
CREATE TABLE leasing_advert_locations
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  location VARCHAR(255),
  CONSTRAINT leasing_advert_locations_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_advert_locations
  OWNER TO leasing;

CREATE TABLE leasing_advert_groups
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  group_id integer NOT NULL,
  CONSTRAINT leasing_advert_groups_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_advert_groups
  OWNER TO leasing;

CREATE TABLE leasing_advert_user_groups
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  group_id integer NOT NULL,
  user_id character varying(64) NOT NULL,
  CONSTRAINT leasing_advert_user_groups_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_advert_user_groups
  OWNER TO leasing;

CREATE TABLE leasing_statuses
(
  id serial NOT NULL,
  status VARCHAR(255),
  CONSTRAINT leasing_statuses_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_statuses
  OWNER TO leasing;

CREATE TABLE leasing_advert_statuses
(
  id serial NOT NULL,
  advert_id integer NOT NULL,
  status_id integer NOT NULL,
  CONSTRAINT leasing_advert_statuses_pkey PRIMARY KEY (id),
  CONSTRAINT leasing_advert_status_id_fkey FOREIGN KEY (status_id)
      REFERENCES leasing_statuses (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE leasing_advert_statuses
  OWNER TO leasing;

CREATE TABLE leasing_group
(
  id serial NOT NULL,
  group_name character varying(255) NOT NULL,
  CONSTRAINT leasing_group_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_group
  OWNER TO leasing;


ALTER TABLE leasing_advert
    ADD CONSTRAINT leasing_advert_type_id_fkey FOREIGN KEY (type_id) REFERENCES leasing_advert(id);

ALTER TABLE leasing_advert
    ADD CONSTRAINT leasing_advert_group_id_fkey FOREIGN KEY (group_id) REFERENCES leasing_group(id);

ALTER TABLE leasing_advert
    ADD CONSTRAINT leasing_advert_created_by_fkey FOREIGN KEY (created_by) REFERENCES leasing_user(user_id);

ALTER TABLE leasing_advert
    ADD CONSTRAINT leasing_advert_updated_by_fkey FOREIGN KEY (updated_by) REFERENCES leasing_user(user_id);

ALTER TABLE leasing_advert
    ADD CONSTRAINT leasing_advert_status_id_fkey FOREIGN KEY (status_id) REFERENCES leasing_statuses(id);

ALTER TABLE leasing_advert_locations
    ADD CONSTRAINT leasing_advert_locations_advert_id_fkey FOREIGN KEY (advert_id) REFERENCES leasing_advert(advert_id);

ALTER TABLE leasing_advert_groups
    ADD CONSTRAINT leasing_advert_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES leasing_group(id);

ALTER TABLE leasing_advert_groups
    ADD CONSTRAINT leasing_advert_groups_advert_id_fkey FOREIGN KEY (advert_id) REFERENCES leasing_advert(advert_id);

ALTER TABLE leasing_advert_user_groups
    ADD CONSTRAINT leasing_advert_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES leasing_group(id);

ALTER TABLE leasing_advert_user_groups
    ADD CONSTRAINT leasing_advert_user_groups_advert_id_fkey FOREIGN KEY (advert_id) REFERENCES leasing_advert(advert_id);

ALTER TABLE leasing_advert_user_groups
    ADD CONSTRAINT leasing_advert_user_groups_user_id_fkey FOREIGN KEY (user_id) REFERENCES leasing_user(user_id);

