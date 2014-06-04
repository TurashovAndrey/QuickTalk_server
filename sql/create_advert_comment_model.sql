CREATE TABLE leasing_advert_comment
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  description VARCHAR(255) NOT NULL,
  from_user_id character varying(64) NOT NULL,
  CONSTRAINT leasing_advert_comment_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_advert_comment
  OWNER TO leasing;

ALTER TABLE leasing_advert_comment
    ADD CONSTRAINT leasing_advert_comment_advert_id_fkey FOREIGN KEY (advert_id) REFERENCES leasing_advert(advert_id);

ALTER TABLE leasing_user_comment
    ADD CONSTRAINT leasing_advert_comment_from_user_id_fkey FOREIGN KEY (from_user_id) REFERENCES leasing_user(user_id);

