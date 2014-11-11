CREATE TABLE job_user_comment
(
  id serial NOT NULL,
  user_id character varying(64) NOT NULL,
  description VARCHAR(255) NOT NULL,
  from_user_id character varying(64) NOT NULL,
  CONSTRAINT job_user_comment_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE job_user_comment
  OWNER TO job;

ALTER TABLE job_user_comment
    ADD CONSTRAINT job_user_comment_user_id_fkey FOREIGN KEY (user_id) REFERENCES job_user(user_id);

ALTER TABLE job_user_comment
    ADD CONSTRAINT job_user_comment_from_user_id_fkey FOREIGN KEY (from_user_id) REFERENCES job_user(user_id);

