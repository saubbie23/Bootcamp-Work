CREATE TABLE IF NOT EXISTS `registration`.`follows` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `users_id` INT(11) NOT NULL,
  `follower_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_follows_users_idx` (`users_id` ASC) VISIBLE,
  INDEX `fk_follows_users1_idx` (`follower_id` ASC) VISIBLE,
  CONSTRAINT `fk_follows_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `registration`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_follows_users1`
    FOREIGN KEY (`follower_id`)
    REFERENCES `registration`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;