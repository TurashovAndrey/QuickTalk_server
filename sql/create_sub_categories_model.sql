CREATE TABLE leasing_advert_sub_categories
(
  id serial NOT NULL,
  category_id integer NOT NULL,
  sub_category_name VARCHAR(255),
  CONSTRAINT leasing_advert_sub_categories_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_advert_sub_categories
  OWNER TO leasing;

ALTER TABLE leasing_advert_sub_categories
    ADD CONSTRAINT leasing_advert_sub_categories_category_id_fkey FOREIGN KEY (category_id) REFERENCES leasing_advert_categories(id);
