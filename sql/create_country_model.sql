CREATE TABLE job_country
(
  id serial NOT NULL,
  country_name character varying(32) DEFAULT NULL::character varying,
  CONSTRAINT job_country_id_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE job_country
  OWNER TO job;
