CREATE TABLE quicktalk_request
(
  id serial NOT NULL,
  request_user_id character varying(64) NOT NULL,
  CONSTRAINT quicktalk_request_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE quicktalk_request
  OWNER TO quicktalk;
                  
ALTER TABLE quicktalk_request
    ADD CONSTRAINT quicktalk_request_request_user_id_fkey FOREIGN KEY (request_user_id) REFERENCES quicktalk_user(user_id);


