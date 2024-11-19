-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dbpython
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dbpython
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dbpython` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
-- -----------------------------------------------------
-- Schema classicmodels
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema classicmodels
-- -----------------------------------------------------
USE `dbpython` ;

-- -----------------------------------------------------
-- Table `dbpython`.`customers_python`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbpython`.`customers_python` (
  `customer_number` INT NOT NULL,
  `customer_fname` VARCHAR(45) NOT NULL,
  `customer_lname` VARCHAR(45) NOT NULL,
  `phone` INT NOT NULL,
  `address1` VARCHAR(100) NOT NULL,
  `address2` VARCHAR(45) NULL DEFAULT NULL,
  `city` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `post_number` INT NOT NULL,
  PRIMARY KEY (`customer_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbpython`.`type_product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbpython`.`type_product` (
  `type_product_code` VARCHAR(15) NOT NULL,
  `type_operation_product` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`type_product_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbpython`.`product_table`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbpython`.`product_table` (
  `product_code` VARCHAR(45) NOT NULL,
  `type_product_code` VARCHAR(15) NOT NULL,
  `product_name` VARCHAR(100) NOT NULL,
  `productDisciption` TEXT NOT NULL,
  `quantity_in_stock` INT NOT NULL,
  `price` INT NOT NULL,
  PRIMARY KEY (`product_code`),
  INDEX `fk_product_type_product1_idx` (`type_product_code` ASC) VISIBLE,
  CONSTRAINT `fk_product_type_product1`
    FOREIGN KEY (`type_product_code`)
    REFERENCES `dbpython`.`type_product` (`type_product_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbpython`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbpython`.`orders` (
  `order_number` INT NOT NULL,
  `order_date` DATE NOT NULL,
  `delivery` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `comment` VARCHAR(45) NULL DEFAULT NULL,
  `customer_number` INT NOT NULL,
  PRIMARY KEY (`order_number`),
  INDEX `fk_orders_customers_python1_idx` (`customer_number` ASC) VISIBLE,
  CONSTRAINT `fk_orders_customers_python1`
    FOREIGN KEY (`customer_number`)
    REFERENCES `dbpython`.`customers_python` (`customer_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbpython`.`order_detail_table`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbpython`.`order_detail_table` (
  `orders_order_number` INT NOT NULL,
  `product_code` VARCHAR(45) NOT NULL,
  `quantity_ordered` INT NOT NULL,
  `price_total_per_order` DECIMAL(10,2) NOT NULL,
  INDEX `fk_order_detail_product1_idx` (`product_code` ASC) VISIBLE,
  PRIMARY KEY (`orders_order_number`),
  CONSTRAINT `fk_order_detail_product1`
    FOREIGN KEY (`product_code`)
    REFERENCES `dbpython`.`product_table` (`product_code`),
  CONSTRAINT `fk_order_detail_table_orders1`
    FOREIGN KEY (`orders_order_number`)
    REFERENCES `dbpython`.`orders` (`order_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbpython`.`payment_table`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbpython`.`payment_table` (
  `customer_number` INT NOT NULL,
  `check_number` VARCHAR(45) NOT NULL,
  `payment_date` DATE NOT NULL,
  `status_payment` VARCHAR(45) NOT NULL,
  `amount` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`customer_number`, `check_number`),
  INDEX `fk_payment_table_customers_python1_idx` (`customer_number` ASC) VISIBLE,
  CONSTRAINT `fk_payment_table_customers_python1`
    FOREIGN KEY (`customer_number`)
    REFERENCES `dbpython`.`customers_python` (`customer_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `classicmodels` ;

-- -----------------------------------------------------
-- Table `classicmodels`.`offices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `classicmodels`.`offices` (
  `officeCode` VARCHAR(10) NOT NULL,
  `city` VARCHAR(50) NOT NULL,
  `phone` VARCHAR(50) NOT NULL,
  `addressLine1` VARCHAR(50) NOT NULL,
  `addressLine2` VARCHAR(50) NULL DEFAULT NULL,
  `state` VARCHAR(50) NULL DEFAULT NULL,
  `country` VARCHAR(50) NOT NULL,
  `postalCode` VARCHAR(15) NOT NULL,
  `territory` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`officeCode`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `classicmodels`.`employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `classicmodels`.`employees` (
  `employeeNumber` INT NOT NULL,
  `lastName` VARCHAR(50) NOT NULL,
  `firstName` VARCHAR(50) NOT NULL,
  `extension` VARCHAR(10) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `officeCode` VARCHAR(10) NOT NULL,
  `reportsTo` INT NULL DEFAULT NULL,
  `jobTitle` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`employeeNumber`),
  INDEX `reportsTo` (`reportsTo` ASC) VISIBLE,
  INDEX `officeCode` (`officeCode` ASC) VISIBLE,
  CONSTRAINT `employees_ibfk_1`
    FOREIGN KEY (`reportsTo`)
    REFERENCES `classicmodels`.`employees` (`employeeNumber`),
  CONSTRAINT `employees_ibfk_2`
    FOREIGN KEY (`officeCode`)
    REFERENCES `classicmodels`.`offices` (`officeCode`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `classicmodels`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `classicmodels`.`customers` (
  `customerNumber` INT NOT NULL,
  `customerName` VARCHAR(50) NOT NULL,
  `contactLastName` VARCHAR(50) NOT NULL,
  `contactFirstName` VARCHAR(50) NOT NULL,
  `phone` VARCHAR(50) NOT NULL,
  `addressLine1` VARCHAR(50) NOT NULL,
  `addressLine2` VARCHAR(50) NULL DEFAULT NULL,
  `city` VARCHAR(50) NOT NULL,
  `state` VARCHAR(50) NULL DEFAULT NULL,
  `postalCode` VARCHAR(15) NULL DEFAULT NULL,
  `country` VARCHAR(50) NOT NULL,
  `salesRepEmployeeNumber` INT NULL DEFAULT NULL,
  `creditLimit` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`customerNumber`),
  INDEX `salesRepEmployeeNumber` (`salesRepEmployeeNumber` ASC) VISIBLE,
  CONSTRAINT `customers_ibfk_1`
    FOREIGN KEY (`salesRepEmployeeNumber`)
    REFERENCES `classicmodels`.`employees` (`employeeNumber`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `classicmodels`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `classicmodels`.`orders` (
  `orderNumber` INT NOT NULL,
  `orderDate` DATE NOT NULL,
  `requiredDate` DATE NOT NULL,
  `shippedDate` DATE NULL DEFAULT NULL,
  `status` VARCHAR(15) NOT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `customerNumber` INT NOT NULL,
  PRIMARY KEY (`orderNumber`),
  INDEX `customerNumber` (`customerNumber` ASC) VISIBLE,
  CONSTRAINT `orders_ibfk_1`
    FOREIGN KEY (`customerNumber`)
    REFERENCES `classicmodels`.`customers` (`customerNumber`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `classicmodels`.`productlines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `classicmodels`.`productlines` (
  `productLine` VARCHAR(50) NOT NULL,
  `textDescription` VARCHAR(4000) NULL DEFAULT NULL,
  `htmlDescription` MEDIUMTEXT NULL DEFAULT NULL,
  `image` MEDIUMBLOB NULL DEFAULT NULL,
  PRIMARY KEY (`productLine`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `classicmodels`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `classicmodels`.`products` (
  `productCode` VARCHAR(15) NOT NULL,
  `productName` VARCHAR(70) NOT NULL,
  `productLine` VARCHAR(50) NOT NULL,
  `productScale` VARCHAR(10) NOT NULL,
  `productVendor` VARCHAR(50) NOT NULL,
  `productDescription` TEXT NOT NULL,
  `quantityInStock` SMALLINT NOT NULL,
  `buyPrice` DECIMAL(10,2) NOT NULL,
  `MSRP` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`productCode`),
  INDEX `productLine` (`productLine` ASC) VISIBLE,
  CONSTRAINT `products_ibfk_1`
    FOREIGN KEY (`productLine`)
    REFERENCES `classicmodels`.`productlines` (`productLine`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `classicmodels`.`orderdetails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `classicmodels`.`orderdetails` (
  `orderNumber` INT NOT NULL,
  `productCode` VARCHAR(15) NOT NULL,
  `quantityOrdered` INT NOT NULL,
  `priceEach` DECIMAL(10,2) NOT NULL,
  `orderLineNumber` SMALLINT NOT NULL,
  PRIMARY KEY (`orderNumber`, `productCode`),
  INDEX `productCode` (`productCode` ASC) VISIBLE,
  CONSTRAINT `orderdetails_ibfk_1`
    FOREIGN KEY (`orderNumber`)
    REFERENCES `classicmodels`.`orders` (`orderNumber`),
  CONSTRAINT `orderdetails_ibfk_2`
    FOREIGN KEY (`productCode`)
    REFERENCES `classicmodels`.`products` (`productCode`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `classicmodels`.`payments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `classicmodels`.`payments` (
  `customerNumber` INT NOT NULL,
  `checkNumber` VARCHAR(50) NOT NULL,
  `paymentDate` DATE NOT NULL,
  `amount` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`customerNumber`, `checkNumber`),
  CONSTRAINT `payments_ibfk_1`
    FOREIGN KEY (`customerNumber`)
    REFERENCES `classicmodels`.`customers` (`customerNumber`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
