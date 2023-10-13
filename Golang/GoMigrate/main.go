package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database/postgres"
	_ "github.com/golang-migrate/migrate/v4/source/file"
	"github.com/marcosban/gomigrate/db"
)


func main() {
	dbMigrate()
}

func dbMigrate() {
	fmt.Println("Levantando configs")
	cfg, err := db.NewConfig()
	dbHost := fmt.Sprintf("Host: %s", cfg.DatabaseHost)
	dbUser := fmt.Sprintf("User: %s", cfg.DatabaseUsername)
	dbPass := fmt.Sprintf("Password: %s", cfg.DatabasePassword)
	fmt.Println(dbHost, dbPass, dbUser)
	
	if err != nil {
		fmt.Println(err)
	}

	connStr := fmt.Sprintf("host=%s user=%s sslmode=disable password=%s",
	cfg.DatabaseHost, cfg.DatabaseUsername, cfg.DatabasePassword)
	
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("Conectou - Dnv")
	driver, err := postgres.WithInstance(db, &postgres.Config{})
	fmt.Println("Conectou - Driver")
	if err != nil {
		fmt.Println(err)
	}

	m, err := migrate.NewWithDatabaseInstance(
        "file://resources/migrations",
        "postgres", driver)
	fmt.Println("Instanciou o migrate")
	if err != nil {
		fmt.Println(err)
	}
	
	m.Up()
	m.Close()
	fmt.Println("Encerrado")
}