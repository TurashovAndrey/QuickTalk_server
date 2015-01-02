CREATE TABLE quicktalk_country
(
  id serial NOT NULL,
  country_name character varying(32) DEFAULT NULL::character varying,
  CONSTRAINT quicktalk_country_id_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE quicktalk_country
  OWNER TO quicktalk;
