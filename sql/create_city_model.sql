CREATE TABLE job_city
(
  id serial NOT NULL,
  city_name character varying(32) DEFAULT NULL::character varying,
  country_id integer NOT NULL,
  CONSTRAINT job_city_id_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_city
    ADD CONSTRAINT job_city_country_id_fkey FOREIGN KEY (country_id) REFERENCES job_country(id);

ALTER TABLE job_city
  OWNER TO job;
