-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema survey
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `survey` ;

-- -----------------------------------------------------
-- Schema survey
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `survey` DEFAULT CHARACTER SET utf8 ;
USE `survey` ;

-- -----------------------------------------------------
-- Table `survey`.`language`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `survey`.`language` ;

CREATE TABLE IF NOT EXISTS `survey`.`language` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `lang` NVARCHAR(100) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `languagecol` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `survey`.`location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `survey`.`location` ;

CREATE TABLE IF NOT EXISTS `survey`.`location` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `locale` NVARCHAR(100) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `survey`.`sex`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `survey`.`sex` ;

CREATE TABLE IF NOT EXISTS `survey`.`sex` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `sex` NVARCHAR(10) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `survey`.`ninja`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `survey`.`ninja` ;

CREATE TABLE IF NOT EXISTS `survey`.`ninja` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `language_id` INT NOT NULL,
  `location_id` INT NOT NULL,
  `sex_id` INT NOT NULL,
  `name` NVARCHAR(100) NULL,
  `comment` NVARCHAR(12) NULL,
  `subscribe` BOOLEAN NULL,
  `create_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninja_language_idx` (`language_id` ASC) VISIBLE,
  INDEX `fk_ninja_location1_idx` (`location_id` ASC) VISIBLE,
  INDEX `fk_ninja_sex1_idx` (`sex_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninja_language`
    FOREIGN KEY (`language_id`)
    REFERENCES `survey`.`language` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ninja_location1`
    FOREIGN KEY (`location_id`)
    REFERENCES `survey`.`location` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ninja_sex1`
    FOREIGN KEY (`sex_id`)
    REFERENCES `survey`.`sex` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
