CREATE TABLE quicktalk_city
(
  id serial NOT NULL,
  city_name character varying(32) DEFAULT NULL::character varying,
  country_id integer NOT NULL,
  CONSTRAINT job_city_id_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE quicktalk_city
    ADD CONSTRAINT quicktalk_city_country_id_fkey FOREIGN KEY (country_id) REFERENCES quicktalk_country(id);

ALTER TABLE quicktalk_city
  OWNER TO quicktalk;
