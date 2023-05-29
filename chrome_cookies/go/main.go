package main

import (
	"fmt"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"net/http/httputil"
	"net"
	"context"
    "strings"
)

type contextKey struct {
	key string
}

var ConnContextKey = &contextKey{"http-conn"}

func SaveConnInContext(ctx context.Context, c net.Conn) context.Context {
	return context.WithValue(ctx, ConnContextKey, c)
}
func GetConn(r *http.Request) net.Conn {
	return r.Context().Value(ConnContextKey).(net.Conn)
}

func main() {
	r := mux.NewRouter()

	r.HandleFunc("/read", xreadCookie).Methods("GET")
	r.HandleFunc("/set", xsetCookie).Methods("GET")
	server := http.Server{
		Addr:    "localhost:8080",
		ConnContext: SaveConnInContext,
		Handler: r,
	}
	log.Println("Server started on: " + server.Addr)
	server.ListenAndServe()
}

func xreadCookie(w http.ResponseWriter, r *http.Request) {
	//fmt.Printf("%T\n",r.Cookie)
	fmt.Println("========= COOKIES =========")
	fmt.Printf("Cookie Header: %s\n", r.Header["Cookie"])
    x := strings.Split(r.Header["Cookie"][0], "=")
    fmt.Printf("Header Code Point: %q\n", x[0])
	for i, c := range r.Cookies() {
		fmt.Printf("Cookies() %d: %s\n", i, c.Name)
	}
	req, err := httputil.DumpRequest(r, true)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("========= REQUEST =========")
	fmt.Println(string(req))
}

func xsetCookie(w http.ResponseWriter, r *http.Request) {
	conn := GetConn(r)
	resp := "HTTP/1.1 200 OK\r\nContent-Length: 0\r\nSet-Cookie: �=set via response\r\n\r\n"
	// how to set actual code point \ud800 ?
	fmt.Fprintf(conn, resp)
	// w.Header().Set("Set-Cookie", rune(0xd800))
	// c := &http.Cookie{
	//         Name:  "\U0000d801",
	//         Value: "x",
	// }
	// http.SetCookie(w, c)
}
