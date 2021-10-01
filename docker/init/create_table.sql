CREATE SCHEMA db_test;

SET search_path=db_test;

CREATE TABLE user_table (
    id INTEGER NOT NULL,
    name VARCHAR(20),
    age INTEGER,
    PRIMARY KEY (id)
) WITHOUT OIDS;

COMMENT ON TABLE user_table IS 'ユーザーテーブル';
COMMENT ON COLUMN user_table.id IS 'ID';
COMMENT ON COLUMN user_table.name IS '名前';
COMMENT ON COLUMN user_table.age IS '年齢';