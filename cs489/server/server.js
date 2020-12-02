const express = require("express");
const app = express();
const api = require("./routes/index");
var cors = require("cors");
const test = require("./routes/test");
const table = require("./routes/table");

app.use(cors());

app.use("/api", api);
app.use("/test", test);
app.use("/table", table);

app.listen(3001, () => console.log("Server is running on port 3001..."));
