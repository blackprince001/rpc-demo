# gRPC with python demo

## Quickstart

Install the package manager and setup a virtual environment with the following commands.

    ```sh
        $ curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    ```sh
    $ uv venv
    $ source .venv/bin/activate
    ```

Install the packages needed into the virtual environment with UV.

    ```sh
        $ uv pip install grpcio
        $ uv pip install grpcio-tools
    ```

## Run the service

From the `py/` directory:

Run the server:

    ```sh
    $ python greeter_server.py
    ```
    From another terminal, run the client:

    ```sh
    $ python greeter_client.py
    ```
    Congratulations! You’ve just run a client-server application with gRPC.

Whenever you change the schema on the proto file, you must regenerate the packaging files. You achieve in this project with this command.

    ```sh
        $ python -m grpc_tools.protoc --proto_path=../proto --python_out=. --pyi_out=. --grpc_python_out=. ./../proto/eatery.proto
    ```
