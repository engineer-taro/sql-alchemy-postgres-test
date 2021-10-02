CREATE SCHEMA db_test;

SET search_path=db_test;

DROP TABLE IF EXISTS user_table;
DROP TABLE IF EXISTS user_score;

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

CREATE TABLE user_score (
    id VARCHAR(50) NOT NULL,
    user_id INTEGER NOT NULL,
    subject VARCHAR(20),
    score INTEGER DEFAULT 50,
    PRIMARY KEY (id)
) WITHOUT OIDS;

COMMENT ON TABLE user_score IS 'ユーザースコアテーブル';
COMMENT ON COLUMN user_score.id IS 'ID';
COMMENT ON COLUMN user_score.user_id IS 'ユーザーID';
COMMENT ON COLUMN user_score.subject IS '科目';
COMMENT ON COLUMN user_score.score IS '点数';