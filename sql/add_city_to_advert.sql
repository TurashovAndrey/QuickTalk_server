ALTER TABLE job_advert
  ADD COLUMN city_id integer;

ALTER TABLE job_advert
    ADD CONSTRAINT job_advert_city_id_fkey FOREIGN KEY (city_id) REFERENCES job_city(id);
