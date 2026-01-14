-- 文字の種類を「utf8mb4」に設定します（日本語を使えるようにするためです）
SET NAMES utf8mb4;

-- もし「menu」という名前のテーブルがすでにある場合は、一度消します
DROP TABLE IF EXISTS menu;

-- 新しく「menu」という名前のテーブル（表）を作ります
CREATE TABLE menu (
    -- メニューの番号です。自動で1, 2, 3と増えるように設定します
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- メニューの名前です。最大255文字まで入るようにします
    name VARCHAR(255) NOT NULL,
    -- 投票数です。最初は「0」が入るように設定します
    count INT DEFAULT 0
);

-- 投票のテストデータをいくつか入れます
INSERT INTO menu (name, count) VALUES
('ハンバーグ', 0),
('生姜焼き', 0),
('サバ味噌', 0),
('カレーライス', 0),
('ラーメン', 0);