CREATE TABLE `users` (
  `id` INT AUTO_INCREMENT,
  `user` VARCHAR(50) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`)
);

ALTER TABLE users ADD INDEX username_index (user);

CREATE TABLE `lists` (
  `id` INT AUTO_INCREMENT,
  `code` VARCHAR(255) NOT NULL,
  `created_at` datetime,
  `user_fk` VARCHAR(255) NOT NULL,
  `data` VARCHAR(5000) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_fk`) REFERENCES users (`user`)
);
