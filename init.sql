SET NAMES utf8mb4;

CREATE TABLE menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    count INT DEFAULT 0
);

-- メニューを大量に追加！
INSERT INTO menu (name, count) VALUES
('A定食 (ハンバーグ)', 0),
('B定食 (生姜焼き)', 0),
('日替わり (サバ味噌)', 0),
('カレーライス', 0),
('カツカレー', 0),
('醤油ラーメン', 0),
('味噌ラーメン', 0),
('きつねうどん', 0),
('かけそば', 0),
('パスタ (ミートソース)', 0),
('親子丼', 0),
('カツ丼', 0),
('サラダバー', 0),
('ソフトクリーム', 0),
('コーヒー', 0);