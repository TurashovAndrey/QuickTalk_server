ALTER TABLE leasing_advert
  ADD COLUMN sub_category_id INTEGER NOT NULL DEFAULT 1;
  
ALTER TABLE leasing_advert
    ADD CONSTRAINT leasing_advert_sub_category_id_fkey FOREIGN KEY (sub_category_id) REFERENCES leasing_advert_sub_categories(id);