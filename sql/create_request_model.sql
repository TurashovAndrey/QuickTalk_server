CREATE TABLE leasing_request
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  request_user_id character varying(64) NOT NULL,
  CONSTRAINT leasing_request_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE leasing_request
  OWNER TO leasing;
                  
ALTER TABLE leasing_request
    ADD CONSTRAINT leasing_request_request_user_id_fkey FOREIGN KEY (request_user_id) REFERENCES leasing_user(user_id);

ALTER TABLE leasing_request
    ADD CONSTRAINT leasing_request_advert_id_fkey FOREIGN KEY (advert_id) REFERENCES leasing_advert(advert_id);

