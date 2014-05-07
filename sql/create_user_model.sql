CREATE TABLE public.leasing_users (
  id SERIAL,
  email varying(32)
)
WITH (oids = false);

ALTER TABLE leasing_users
  OWNER TO leasing;
