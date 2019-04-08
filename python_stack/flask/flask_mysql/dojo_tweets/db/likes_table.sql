CREATE TABLE IF NOT EXISTS `registration`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `users_id` INT NOT NULL,
  `tweets_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_likes_users1_idx` (`users_id` ASC) VISIBLE,
  INDEX `fk_likes_tweets1_idx` (`tweets_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `registration`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_tweets1`
    FOREIGN KEY (`tweets_id`)
    REFERENCES `registration`.`tweets` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)