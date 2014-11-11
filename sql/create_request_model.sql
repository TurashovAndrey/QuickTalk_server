CREATE TABLE job_request
(
  id serial NOT NULL,
  advert_id character varying(64) NOT NULL,
  request_user_id character varying(64) NOT NULL,
  CONSTRAINT job_request_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_request
  OWNER TO job;
                  
ALTER TABLE job_request
    ADD CONSTRAINT job_request_request_user_id_fkey FOREIGN KEY (request_user_id) REFERENCES job_user(user_id);

ALTER TABLE job_request
    ADD CONSTRAINT job_request_advert_id_fkey FOREIGN KEY (advert_id) REFERENCES job_advert(advert_id);

