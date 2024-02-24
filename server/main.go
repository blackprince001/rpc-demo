package main

import (
	"context"
	"fmt"
	"log"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	"github.com/blackprince001/rpc-demo/eatery"
)

type server struct {
	eatery.UnimplementedEarteryServer
}

func (s *server) BuyGobe(
	ctx context.Context, in *eatery.MenuRequest,
) (*eatery.MenuResponse, error) {
	total_cost := in.Beans + in.Plantain + in.Rice
	if in.Vegetables {
		return &eatery.MenuResponse{
			Message: fmt.Sprintf(
				"Gobe Cost - %d. You bought Gobe with Veges!", total_cost),
		}, nil
	}
	return &eatery.MenuResponse{
		Message: fmt.Sprintf(
			"Gobe Cost - %d. You bought Gobe without Veges!", total_cost),
	}, nil
}

func main() {
	listener, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	s := grpc.NewServer()
	reflection.Register(s)

	log.Println("Trying to serve on port 50051")

	eatery.RegisterEarteryServer(s, &server{})
	if err := s.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}

}
