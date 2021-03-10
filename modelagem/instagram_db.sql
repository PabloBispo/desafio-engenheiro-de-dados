CREATE TABLE `user` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(60) NOT NULL,
	`username` varchar(25) NOT NULL UNIQUE,
	`bio` varchar(90),
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `post` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`post_caption` VARCHAR(255),
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `commentary` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`comment` VARCHAR(255),
	`user_id` INT NOT NULL,
	`post_id` INT NOT NULL,
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `image` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`album_id` INT NOT NULL,
	`url` varchar NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `album` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`post_id` INT NOT NULL,
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `friendship` (
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`user_id` INT NOT NULL,
	`follower_id` INT NOT NULL,
	`is_active` BINARY NOT NULL DEFAULT true,
	PRIMARY KEY (`user_id`,`follower_id`)
);

CREATE TABLE `like` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`post_id` INT,
	`commentary_id` INT,
	`is_liked` BINARY NOT NULL DEFAULT false,
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

ALTER TABLE `post` ADD CONSTRAINT `post_fk0` FOREIGN KEY (`user_id`) REFERENCES `user`(`id`);

ALTER TABLE `commentary` ADD CONSTRAINT `commentary_fk0` FOREIGN KEY (`user_id`) REFERENCES `user`(`id`);

ALTER TABLE `commentary` ADD CONSTRAINT `commentary_fk1` FOREIGN KEY (`post_id`) REFERENCES `post`(`user_id`);

ALTER TABLE `image` ADD CONSTRAINT `image_fk0` FOREIGN KEY (`album_id`) REFERENCES `album`(`id`);

ALTER TABLE `album` ADD CONSTRAINT `album_fk0` FOREIGN KEY (`post_id`) REFERENCES `post`(`id`);

ALTER TABLE `friendship` ADD CONSTRAINT `friendship_fk0` FOREIGN KEY (`user_id`) REFERENCES `user`(`id`);

ALTER TABLE `friendship` ADD CONSTRAINT `friendship_fk1` FOREIGN KEY (`follower_id`) REFERENCES `user`(`id`);

ALTER TABLE `like` ADD CONSTRAINT `like_fk0` FOREIGN KEY (`user_id`) REFERENCES `user`(`id`);

ALTER TABLE `like` ADD CONSTRAINT `like_fk1` FOREIGN KEY (`post_id`) REFERENCES `post`(`id`);

ALTER TABLE `like` ADD CONSTRAINT `like_fk2` FOREIGN KEY (`commentary_id`) REFERENCES `commentary`(`post_id`);
