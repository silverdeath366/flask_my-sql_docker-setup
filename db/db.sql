CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);

INSERT INTO users (name, email) VALUES ('yakov', 'yakov$@walla.com');
INSERT INTO users (name, email) VALUES ('moshe', 'moshe*@yahoo.com');
