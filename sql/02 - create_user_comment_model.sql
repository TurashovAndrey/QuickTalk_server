CREATE TABLE quicktalk_user_comment
(
  id serial NOT NULL,
  user_id character varying(64) NOT NULL,
  description VARCHAR(255) NOT NULL,
  from_user_id character varying(64) NOT NULL,
  CONSTRAINT quicktalk_user_comment_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE quicktalk_user_comment
  OWNER TO quicktalk;

ALTER TABLE quicktalk_user_comment
    ADD CONSTRAINT quicktalk_user_comment_user_id_fkey FOREIGN KEY (user_id) REFERENCES quicktalk_user(user_id);

ALTER TABLE quicktalk_user_comment
    ADD CONSTRAINT quicktalk_user_comment_from_user_id_fkey FOREIGN KEY (from_user_id) REFERENCES quicktalk_user(user_id);

