CREATE TABLE `users` (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `id_google` VARCHAR(50) NOT NULL,
  `picture` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
);

ALTER TABLE users ADD INDEX id_google_index (id_google);

CREATE TABLE `lists` (
  `id` INT AUTO_INCREMENT,
  `code` VARCHAR(255) NOT NULL,
  `created_at` VARCHAR(255) NOT NULL,
  `user_id_google` VARCHAR(255) NOT NULL,
  `data` VARCHAR(65535) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id_google`) REFERENCES users (`id_google`)
);
