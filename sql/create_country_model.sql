CREATE TABLE leasing_country
(
  id serial NOT NULL,
  country_name character varying(32) DEFAULT NULL::character varying,
  CONSTRAINT leasing_country_id_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE leasing_country
  OWNER TO leasing;
