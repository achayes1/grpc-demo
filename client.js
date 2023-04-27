const grpc = require("@grpc/grpc-js");
var protoLoader = require("@grpc/proto-loader");
const PROTO_PATH = "./test_grpc_service.proto";

const options = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
};

var packageDefinition = protoLoader.loadSync(PROTO_PATH, options);

const TestGrpcService = grpc.loadPackageDefinition(packageDefinition).TestGrpcService;

const client = new TestGrpcService(
  "localhost:50051",
  grpc.credentials.createInsecure()
);

function callGrpcApi () {
    client.TestGrpcApiRoute({message: "ping from node"}, (error, data) => {
        if (error) throw error
        const { message } = data
        console.log(message);
    });
}

function main () {
    callGrpcApi()
}

main()