ALTER TABLE leasing_advert
  ADD COLUMN city_id integer;

ALTER TABLE leasing_advert
    ADD CONSTRAINT leasing_advert_city_id_fkey FOREIGN KEY (city_id) REFERENCES leasing_city(id);
