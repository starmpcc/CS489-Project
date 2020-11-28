const express = require("express");
const app = express();
const api = require("./routes/index");
var cors = require("cors");

app.use(cors());

app.use("/api", api);

app.listen(3001, () => console.log("Server is running on port 3001..."));
