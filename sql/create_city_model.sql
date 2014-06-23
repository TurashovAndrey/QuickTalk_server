CREATE TABLE leasing_city
(
  id serial NOT NULL,
  city_name character varying(32) DEFAULT NULL::character varying,
  country_id integer NOT NULL,
  CONSTRAINT leasing_city_id_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_city
    ADD CONSTRAINT leasing_city_country_id_fkey FOREIGN KEY (country_id) REFERENCES leasing_country(id);

ALTER TABLE leasing_city
  OWNER TO leasing;
