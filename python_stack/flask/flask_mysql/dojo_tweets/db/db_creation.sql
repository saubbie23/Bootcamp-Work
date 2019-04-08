-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema registration
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `registration` ;

-- -----------------------------------------------------
-- Schema registration
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `registration` DEFAULT CHARACTER SET utf8 ;
USE `registration` ;

-- -----------------------------------------------------
-- Table `registration`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `registration`.`users` ;

CREATE TABLE IF NOT EXISTS `registration`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` NVARCHAR(50) NULL,
  `last_name` NVARCHAR(50) NULL,
  `email` NVARCHAR(255) NULL,
  `password` NVARCHAR(50) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `registration`.`tweets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `registration`.`tweets` ;

CREATE TABLE IF NOT EXISTS `registration`.`tweets` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `users_id` INT NOT NULL,
  `tweet` NVARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tweets_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_tweets_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `registration`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
