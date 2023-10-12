package db

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

func init() {
	fmt.Println("Vai conectar o DB")
}

func writeDb() {
	connStr := "host=db-app user=postgres dbname=dbclients sslmode=disable password=Postgres2022!"
	dbInsert := `
	INSERT INTO clients ( "CPF", "Email", "Name")
	VALUES ($1, $2, $3)
	`
	fmt.Println("Entrou na função!")
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	for _, a := range clients {
		db.Exec(dbInsert, a.CPF, a.Email, a.Name)
	}
}

func getDbconnect(c *gin.Context) {
	connStr := "host=db-app user=postgres dbname=dbclients sslmode=disable password=Postgres2022!"
	db, err := sql.Open("postgres", connStr)
	sqlStatement, err := db.Query("SELECT * FROM clients")

	if err != nil {
		log.Fatal(err)
	}
	//var message = "É pra conectar"
	c.JSON(http.StatusOK, sqlStatement)
}
