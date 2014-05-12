CREATE TABLE leasing_user
(
  id serial NOT NULL,
  user_id character varying(64) DEFAULT NULL::character varying,
  username character varying(50) DEFAULT NULL::character varying,
  hashed_pw character varying(128) DEFAULT NULL::character varying,
  first_name character varying(32) DEFAULT NULL::character varying,
  last_name character varying(32) DEFAULT NULL::character varying,
  email character varying(32) DEFAULT NULL::character varying,
  created integer,
  created_ip character varying(39) DEFAULT NULL::character varying,
  updated integer,
  updated_ip character varying(39) DEFAULT NULL::character varying,
  birthday date,
  hometown character varying(80),
  location character varying(250),
  bio character varying,
  gender character varying(15),
  is_active boolean NOT NULL DEFAULT true,
  is_deleted boolean NOT NULL DEFAULT false,
  telephone character varying,
  CONSTRAINT leasing_user_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE leasing_user
  OWNER TO leasing;

CREATE UNIQUE INDEX leasing_user_user_id_idx ON leasing_user(user_id);