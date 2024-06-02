CREATE TABLE census (
    age INT NOT NULL,
    workclass VARCHAR(50) NOT NULL,
    fnlwgt INT NOT NULL,
    education VARCHAR(20) NOT NULL,
    educational_grade VARCHAR(50) NOT NULL,
    marital_status VARCHAR(50) NOT NULL,
    occupation VARCHAR(50) NOT NULL,
    relationship VARCHAR(50) NOT NULL,
    race VARCHAR(20) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    capital_gain INT NOT NULL,
    capital_loss INT NOT NULL,
    hours_worked_per_week INT NOT NULL,
    native_country VARCHAR(100) NOT NULL,
    annual_income VARCHAR(20) NOT NULL
);

ALTER TABLE census
ALTER COLUMN educational_grade TYPE INT USING educational_grade::INTEGER;

ALTER TABLE census
ADD COLUMN censusID INT GENERATED ALWAYS AS IDENTITY;

CREATE INDEX idx_censusID ON census (censusID);

ALTER TABLE census
ADD CONSTRAINT censusID_pkey PRIMARY KEY (censusID);

SELECT * FROM census;

CREATE TABLE education (
	education VARCHAR(20) NOT NULL,
    educational_grade INT NOT NULL,
	UNIQUE (education, educational_grade),
	CONSTRAINT pk_education PRIMARY KEY (
        educational_grade
     )
);

SELECT * FROM education;

INSERT INTO education (education, educational_grade)
SELECT DISTINCT education, educational_grade
FROM census;

SELECT *
FROM education
ORDER BY educational_grade ASC;

CREATE TABLE marital_status (
	marital_status VARCHAR(50) NOT NULL,
	UNIQUE (marital_status),
	CONSTRAINT pk_marital_status PRIMARY KEY (
        marital_status
     )
);

SELECT * FROM marital_status;

INSERT INTO marital_status (marital_status)
SELECT DISTINCT marital_status
FROM census;

SELECT *
FROM marital_status
ORDER BY marital_status ASC;

CREATE TABLE country (
	native_country VARCHAR(100) NOT NULL,
	UNIQUE (native_country),
	CONSTRAINT pk_country PRIMARY KEY (
        native_country
     )
);

SELECT * FROM country;

INSERT INTO country (native_country)
SELECT DISTINCT native_country
FROM census;

SELECT *
FROM country
ORDER BY native_country ASC;

CREATE TABLE workclass (
	workclass VARCHAR(50) NOT NULL,
	UNIQUE (workclass),
	CONSTRAINT pk_workclass PRIMARY KEY (
        workclass
     )
);

SELECT * FROM workclass;

INSERT INTO workclass (workclass)
SELECT DISTINCT workclass
FROM census;

SELECT *
FROM workclass
ORDER BY workclass ASC;

CREATE TABLE occupation (
	occupation VARCHAR(50) NOT NULL,
	UNIQUE (occupation),
	CONSTRAINT pk_occupation PRIMARY KEY (
        occupation
     )
);

SELECT * FROM occupation;

INSERT INTO occupation (occupation)
SELECT DISTINCT occupation
FROM census;

SELECT *
FROM occupation
ORDER BY occupation ASC;

CREATE TABLE race (
	race VARCHAR(20) NOT NULL,
	UNIQUE (race),
	CONSTRAINT pk_race PRIMARY KEY (
    	race
     )
);

SELECT * FROM race;

INSERT INTO race (race)
SELECT DISTINCT race
FROM census;

SELECT *
FROM race
ORDER BY race ASC;

CREATE TABLE gender (
	gender VARCHAR(20) NOT NULL,
	UNIQUE (gender),
	CONSTRAINT pk_gender PRIMARY KEY (
        gender
     )
);

SELECT * FROM gender;

INSERT INTO gender (gender)
SELECT DISTINCT gender
FROM census;

ALTER TABLE census ADD CONSTRAINT fk_census_workclass FOREIGN KEY(workclass)
REFERENCES workclass (workclass);

ALTER TABLE census ADD CONSTRAINT fk_census_educational_grade FOREIGN KEY(educational_grade)
REFERENCES education (educational_grade);

ALTER TABLE census ADD CONSTRAINT fk_census_marital_status FOREIGN KEY(marital_status)
REFERENCES marital_status (marital_status);

ALTER TABLE census ADD CONSTRAINT fk_census_occupation FOREIGN KEY(occupation)
REFERENCES occupation (occupation);

ALTER TABLE census ADD CONSTRAINT fk_census_race FOREIGN KEY(race)
REFERENCES race (race);

ALTER TABLE census ADD CONSTRAINT fk_census_gender FOREIGN KEY(gender)
REFERENCES gender (gender);

ALTER TABLE census ADD CONSTRAINT fk_census_native_country FOREIGN KEY(native_country)
REFERENCES country (native_country);