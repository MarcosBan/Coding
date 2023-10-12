package main

import (
	"net/http"

	"github.com/gin-gonic/gin"

	_ "github.com/lib/pq"
)

// album represents data about a record album.
type client struct {
	CPF   string
	Name  string
	Email string
}

// clients slice to seed record album data.
var clients = []client{
	{CPF: "123456719", Name: "John Coltrane", Email: "john@mail.com"},
	{CPF: "123486789", Name: "Gerry Mulligan", Email: "gerry@mail.com"},
	{CPF: "123496789", Name: "Sarah Vaughan", Email: "sarah@mail.com"},
	{CPF: "123496789", Name: "Taaol Do Cliente", Email: "cliente@mail.com"},
}

func main() {
	router := gin.Default()
	router.GET("/clients", getClients)
	//router.GET("/clients/:id", getClientsByID)
	router.GET("/dbconnect", getDbconnect)
	router.POST("/clients", postClients)
	router.Run("0.0.0.0:8080")
}

// getClients responds with the list of all clients as JSON.
func getClients(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, clients)
}

// postclients adds an album from JSON received in the request body.
func postClients(c *gin.Context) {
	var newClient client

	// Call BindJSON to bind the received JSON to
	// newAlbum.
	if err := c.BindJSON(&newClient); err != nil {
		return
	}

	// Add the new album to the slice.
	clients = append(clients, newClient)
	c.IndentedJSON(http.StatusCreated, newClient)
}

// getClientsByID locates the album whose ID value matches the id
// parameter sent by the client, then returns that clients as a response.
// func getClientsByID(c *gin.Context) {
// 	id := c.Param("id")

// 	// Loop through the list of clients, looking for
// 	// an clients whose ID value matches the parameter.
// 	for _, a := range clients {
// 		if a.ID == id {
// 			c.IndentedJSON(http.StatusOK, a)
// 			return
// 		}
// 	}
// 	c.IndentedJSON(http.StatusNotFound, gin.H{"message": "client not found"})
// }
