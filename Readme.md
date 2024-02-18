# gRPC with Golang demo

## Quickstart

In order to install protobuf on your own machine, you can use the following commands

    ```sh
    $ go install google.golang.org/grpc/cmd/protoc-gen-go@v1.28
    $ go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1
    ```

Download a client for your gRPC backend:

    ```sh
       $ go install github.com/fullstorydev/grpcui/cmd/grpcui@latest
    ```

You would also have to setup a protobuf compiler on your local machine and you would install that with the following command according to the platform you work on:

Linux, using apt or apt-get, for example:

    ```sh
    $ apt install -y protobuf-compiler
    $ protoc --version  # Ensure compiler version is 3+
    ```

MacOS, using Homebrew:

    ```sh
    $ brew install protobuf
    $ protoc --version  # Ensure compiler version is 3+
    ```

## Run the service

From the `server/` directory:

Run the server:

    ```sh
    $ go run server/main.go
    ```
    From another terminal, run the client:

    ```sh
    $ grpcui --plaintext localhost:50051
    ```

    The server port and address running locally have already been set on the `server/main.go` file.

    Congratulations! You’ve just run a client-server application with gRPC.

Whenever you change the schema on the proto file, you must regenerate the packaging files. You achieve in this project with this command.

    ```sh
        $ protoc --proto_path=proto proto/*.proto --go_out=. --go-grpc_out=.
    ```

Check out the docs for setting up the Python gRPC server: [Python gRPC](py/Readme.md)
